#!/usr/bin/env python3
"""Збирає навчальні матеріали (Markdown) у HTML і PDF з кольоровими блоками.

Використання:
    python tools/build_materials.py materials/day-1/day-1-instruction.md [ще файли...]
        [--teacher]   показати розділи для викладача/ментора (за замовчуванням їх приховано)
        [--pdf]       додатково зробити PDF через Microsoft Edge або Chrome (headless)
        [--out build] папка результату

Потрібен пакет: pip install markdown
"""
import argparse
import html
import os
import re
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(HERE, 'materials.css')

# Початок абзацу (після **) -> клас кольору
MARKERS = [
    ("**КОПІЮЙТЕ", 'c-copy'),
    ("**У ЧАТ CURSOR", 'c-chat'),
    ("**У FIGMA MAKE", 'c-figma'),
    ("**ПЕРЕВІРТЕ", 'c-check'),
    ("**ЯКЩО НЕ ВИЙШЛО", 'c-fail'),
    ("**БЕЗПЕКА", 'c-safety'),
    ("**Здача", 'c-deliver'),
    ("**Обов'язкове", 'c-deliver'),
    ("**Обов’язкове", 'c-deliver'),
    ("*Орієнтир", 'c-hint'),
]

TEACHER_HEADING = re.compile(r'^(#{1,6})\s+(.*(Для викладача|Критерії перевірки \(ментору\)|Для менторів|Для куратора).*)$')

ROW_CLASSES = {
    'КОПІЮЙТЕ': 'row-c-copy',
    'У ЧАТ CURSOR': 'row-c-chat',
    'У FIGMA MAKE': 'row-c-figma',
    'ПЕРЕВІРТЕ': 'row-c-check',
    'ЯКЩО НЕ ВИЙШЛО': 'row-c-fail',
    'БЕЗПЕКА': 'row-c-safety',
    "ОБОВ'ЯЗКОВЕ": 'row-c-deliver',
    'ОБОВ’ЯЗКОВЕ': 'row-c-deliver',
    'ОРІЄНТИР': 'row-c-hint',
}


def color_legend_table(body):
    """Фарбує рядки таблиці «Як користуватися інструкцією» за позначкою в першій клітинці."""
    m = re.search(r'(<h2[^>]*>Як користуватися інструкцією</h2>\s*)<table>(.*?)</table>', body, re.S)
    if not m:
        return body
    table = m.group(2)

    def row(rm):
        cell = re.search(r'<td[^>]*>(.*?)</td>', rm.group(1), re.S)
        key = re.sub(r'<[^>]+>', '', cell.group(1)).strip() if cell else ''
        cls = ROW_CLASSES.get(key)
        return ('<tr class="%s">' % cls if cls else '<tr>') + rm.group(1) + '</tr>'

    table = re.sub(r'<tr>(.*?)</tr>', row, table, flags=re.S)
    return body[:m.start()] + m.group(1) + '<table class="legend-table">' + table + '</table>' + body[m.end():]


def split_blocks(text):
    """Ділить Markdown на блоки: заголовок / огороджений код / решта (абзац, список, таблиця, цитата)."""
    lines = text.split('\n')
    blocks, cur, in_fence = [], [], False
    for line in lines:
        if line.strip().startswith('```'):
            if not in_fence:
                if cur:
                    blocks.append(('para', '\n'.join(cur)))
                    cur = []
                in_fence = True
                cur.append(line)
            else:
                cur.append(line)
                blocks.append(('fence', '\n'.join(cur)))
                cur = []
                in_fence = False
            continue
        if in_fence:
            cur.append(line)
            continue
        if line.strip() == '':
            if cur:
                blocks.append(('para', '\n'.join(cur)))
                cur = []
            continue
        if re.match(r'^#{1,6}\s', line) and not cur:
            blocks.append(('heading', line))
            continue
        cur.append(line)
    if cur:
        blocks.append(('fence' if in_fence else 'para', '\n'.join(cur)))
    return blocks


def is_list(block):
    return re.match(r'^(\s*[-*]\s|\s*\d+\.\s)', block[1].split('\n')[0]) is not None


LIST_LINE = re.compile(r'^\s*([-*+]|\d+\.)\s+')


def fix_lists(body):
    """Python-Markdown вимагає порожнього рядка перед списком: додаємо його."""
    out = []
    prev = ''
    for line in body.split('\n'):
        if LIST_LINE.match(line) and prev.strip() and not LIST_LINE.match(prev) and not prev.startswith('>') and not prev.startswith('|') and not prev.startswith(' '):
            out.append('')
        out.append(line)
        prev = line
    return '\n'.join(out)


def transform(text, teacher):
    blocks = [(k, fix_lists(b) if k == 'para' else b) for k, b in split_blocks(text)]
    out = []
    i = 0
    skip_level = None
    first_quote_done = False
    while i < len(blocks):
        kind, body = blocks[i]
        # розділи для викладача
        if kind == 'heading':
            m = TEACHER_HEADING.match(body)
            level = len(body) - len(body.lstrip('#'))
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if m and not teacher:
                skip_level = level
                i += 1
                continue
        if skip_level is not None:
            i += 1
            continue
        if kind == 'para' and body.lstrip().startswith('>'):
            first_line = body.lstrip()[1:].strip()
            if not teacher and (first_line.startswith('ЧЕРНЕТКА') or first_line.startswith('**Для викладача') or first_line.startswith('Для викладача')):
                i += 1
                continue
        # кольорові маркери
        if kind == 'para':
            cls = None
            stripped = body.lstrip()
            for prefix, c in MARKERS:
                if stripped.startswith(prefix):
                    cls = c
                    break
            if cls:
                group = [body]
                if i + 1 < len(blocks):
                    nkind, nbody = blocks[i + 1]
                    if nkind == 'fence' or (nkind == 'para' and is_list(blocks[i + 1])):
                        group.append(nbody)
                        i += 1
                out.append('<div class="callout %s" markdown="1">\n\n%s\n\n</div>' % (cls, '\n\n'.join(group)))
                i += 1
                continue
        out.append(body)
        i += 1
    return '\n\n'.join(out) + '\n'


def render(md_path, teacher):
    text = open(md_path, encoding='utf8').read()
    text = transform(text, teacher)
    body = markdown.markdown(text, extensions=['extra', 'md_in_html', 'sane_lists', 'toc'])
    title = os.path.splitext(os.path.basename(md_path))[0]
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1))
    css = open(CSS_PATH, encoding='utf8').read()
    body = color_legend_table(body)
    return '<!doctype html>\n<html lang="uk"><head><meta charset="utf-8">' \
           '<meta name="viewport" content="width=device-width, initial-scale=1">' \
           '<title>%s</title><style>%s</style></head><body>%s</body></html>' % (html.escape(title), css, body)


def find_browser():
    candidates = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None


def to_pdf(html_path, pdf_path):
    browser = find_browser()
    if not browser:
        print('Не знайдено Edge або Chrome для PDF', file=sys.stderr)
        return False
    uri = 'file:///' + os.path.abspath(html_path).replace('\\', '/')
    import tempfile
    profile = tempfile.mkdtemp(prefix='materials-pdf-')
    cmd = [browser, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
           '--user-data-dir=' + profile,
           '--print-to-pdf=' + os.path.abspath(pdf_path), uri]
    subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    return os.path.exists(pdf_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    ap.add_argument('--teacher', action='store_true')
    ap.add_argument('--pdf', action='store_true')
    ap.add_argument('--out', default='build')
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    for f in args.files:
        name = os.path.splitext(os.path.basename(f))[0] + ('-teacher' if args.teacher else '')
        html_path = os.path.join(args.out, name + '.html')
        open(html_path, 'w', encoding='utf8').write(render(f, args.teacher))
        print('HTML:', html_path)
        if args.pdf:
            pdf_path = os.path.join(args.out, name + '.pdf')
            print('PDF:', pdf_path, 'OK' if to_pdf(html_path, pdf_path) else 'не вдалося')


if __name__ == '__main__':
    main()
