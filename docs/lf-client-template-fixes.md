# Виправлення шаблонного репозиторію lf-client (для підготовки шаблону)

Перевірено на чистій копії з архіву `session-01-03modified-liatoshynsky.zip` (Node 24, npm 12). Запуск працює: `npm install`, `npm run dev`, сторінки `/en`, `/en/about-us`, `/en/contacts` віддають 200, `POST /api/contact` повертає `success: true`.

До виправлень `npm test` падав (`bail: 1` зупиняв на першому провалі). Рішення: `bail: 1` залишаємо, тести виправляємо. Після виправлень: **290 наборів, 1434 тести, усі проходять**.

## Зміни в тестах (код застосунку не змінювався)

| Файл | Проблема | Виправлення |
|---|---|---|
| `app/shared/hooks/query/useMutation.test.tsx` | Версія TanStack Query у lock-файлі (5.100.8) викликає `mutationFn` з другим аргументом (контекстом); тест очікував один | Три перевірки: `toHaveBeenCalledWith('…', expect.anything())` |
| `app/api/blob-url/route.test.ts` | Під `jsdom` немає глобального `Response`, а `next/server` його потребує; очікування застаріли (503 «Blob storage is disabled…») порівняно з route (404 «No mock blob found: …») | Додано `@jest-environment node`; оновлено очікування й назву тесту |
| `app/services/upload/upload.test.ts` | Те саме з `Response`; очікування застаріли (503) | Додано `@jest-environment node`; тест перевіряє redirect (302) і заголовок `location` з абсолютним URL |

## Помічено, але не змінювалося
- `streamBlob()` у `app/services/upload/upload.ts` без аргументу падає: `Response.redirect` вимагає абсолютний URL, а `toDemoBlobUrl()` повертає відносний шлях. Функція в застосунку не використовується. Важливо для сесії 3: вправа з вкладенням файлу спиратиметься на `app/services/upload/`.
- У `package.json` немає `engines` (README вимагає Node 22); `.npmrc` містить налаштування, про які npm 12 попереджає (`minimum-release-age`, `block-exotic-subdeps`, `verify-store-integrity`).
- README пропонує клонувати `ba-training-2026-05/lf-client`, тоді як сесії кажуть створити копію з шаблону. Розділ README перепишемо, коли буде готовий наш репозиторій.

## Статус
Виправлення застосовано лише в локальній робочій копії (`scratchpad`). У шаблонний репозиторій їх ще не перенесено, бо його ще немає.
