# Набір для Cursor: агенти й skills курсу

> ЧЕРНЕТКА v1. Перенесено з Claude-версії (`.claude/agents`, `.claude/skills` з Order Desk) на формат Cursor: `.cursor/agents/*.md` і `.cursor/skills/*/SKILL.md`, з YAML-заголовком і українським текстом. **Не перевірено в самому Cursor** (не запускалось): формат заголовків узято з Session 2 (`name`, `description`, `model: inherit`, `readonly`). Перевірити на прогоні, що Cursor підхоплює файли й що виклик за назвою працює.

## Що всередині

**Агенти** (`.cursor/agents/`), викликаються за назвою (`/назва` або словами):

| Агент | Для чого | День |
|---|---|---|
| `ba-docs` | Документація фічі: трасування, user stories, діаграма, Humanizer (опційна частина дня 2) | 2 |
| `ba-poc-guide` | Безпечний sandbox-PoC | 3 |
| `seed-data-scout` | Пошук seed-даних | 3 |
| `validation-tracer` | Трасування валідації (UI/API/схема/тести) | 3 |
| `diff-business-explainer` | Пояснення diff бізнес-мовою | 3 |
| `poc-evidence-reviewer` | Доведено / не доведено / потрібен розробник | 3 |
| `stakeholder-summary-writer` | Підсумок PoC для стейкхолдерів | 3 |
| `feature-flag-scout` | Пошук feature flags | 3 |

**Skills** (`.cursor/skills/`): `humanizer`, `codebase-scout`, `diff-explainer`, `feature-flag-advisor`, `poc-validator`, `safe-change-review`, `stakeholder-summary`, `validation-tracer`.

`readonly: true` мають агенти, які лише читають код і нічого не змінюють (`seed-data-scout`, `validation-tracer`, `diff-business-explainer`, `poc-evidence-reviewer`, `feature-flag-scout`).

## Як використовувати

1. Скопіюйте папку `.cursor` із цього набору в корінь шаблонного репозиторію lf-client (або дайте учасникам зробити це за інструкцією).
2. Перезапустіть Cursor.
3. Викличте агента: наприклад, `/ba-docs Задокументуй фічу «Новини». Збережи в docs/news-feature.md.`
4. Skill підключайте словами: «Застосуй skill humanizer до docs/about-us-feature.md».

Усі вправи курсу виконуються й **без** цього набору звичайними промптами. Набір це зручність, а не вимога.

> **Безпека:** skill це текстовий файл, який стає інструкціями для агента. Не підключайте чужі skills, не прочитавши їх (чи немає в них зовнішніх посилань, доступу до `.env` або команд оболонки). Усі файли цього набору написані для курсу й не містять зовнішніх посилань.

## Чого тут немає (прогалини)

- Агентів і skills сесії 5 (`figma-flow-inspector`, `refinement-question-generator`, `design-to-code-scout`, `component-pattern-reviewer`, `accessibility-reviewer`, `prototype-scope-reviewer`, `implementation-impact-analyzer`, `handoff-pack-writer`; skills `figma-flow-analysis`, `ui-consistency-review`, `refinement-validator`, `prototype-humanizer`, `accessibility-review`, `component-mapping`): їхнього вмісту немає в наданих матеріалах (лише назви й промпти в Session 5). За потреби їх треба написати.
- Правила `.cursor/rules/docs-ba.mdc`: учасники створюють його самі в дні 2.
- Humanizer у Session 2 було запропоновано завантажити із зовнішнього репозиторію; тут використано коротку локальну версію з Order Desk (без зовнішнього завантаження).

## Для викладача

- [ ] Перевірити в Cursor: виклик `/ba-docs`, підхоплення `readonly`, застосування skills.
- [ ] Вирішити, чи розкладати набір у шаблонний репозиторій заздалегідь, чи нехай учасники копіюють на дні 2–3.
- [ ] Вирішити, чи писати агентів/skills сесії 5.
