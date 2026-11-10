# Тексти для issue (запасний приклад, день 2)

> ЗАПАСНИЙ ПРИКЛАД. Якщо GitHub MCP або чат недоступні, ці тексти можна **прочитати, виправити й вставити вручну** на github.com. Опора: `contact-form-feature.md` у цій же папці. Додайте власні правки (див. `materials/fallback/README.md`).

## 1. Створення issue

**Заголовок:** `Contact form — update validation and notifications`

**Тіло:**

```text
We want to tighten up the contact form. Phone number should be mandatory.
We should also let visitors attach a document (CV or portfolio) when they write to us.
Notifications need to reflect the new field.
```

## 2. Коментар «Rules table:»

| Правило | Файл | Джерело істини | Шар |
|---|---|---|---|
| Ім'я 2–50 символів | `validation.ts`, `validateContactData.ts`; `ContactForm.tsx` | константа / число в схемі | API і UI |
| Email | `validateContactData.ts` (регулярний вираз); `ContactForm.tsx` (`.email()`) | **два різні правила** | API і UI |
| Телефон необов'язковий; формат `+` і цифри, 11–16 | `validateContactData.ts`; `ContactForm.tsx` | регулярний вираз / схема | API і UI |
| Повідомлення 10–1000 | `validation.ts`; `ContactForm.tsx`; `i18n/messages` | константа і число в схемі й текстах | API і UI |
| Згода з політикою обов'язкова | `ContactForm.tsx` | схема zod | **лише UI** |
| Запит «приймається» у демо-режимі | `app/api/collaboration/route.ts` | жорстко закодований текст | API |

## 3. Коментар з аналізом впливу

| Зачеплена область | Тип зміни | Ризик | Рекомендована дія | Ідея регресійного тесту |
|---|---|---|---|---|
| Форма (`ContactForm.tsx`) | змінена | середній | Зробити телефон обов'язковим, додати поле файлу | Порожній телефон не відправляється |
| Валідація API (`validateContactData.ts`) | змінена | високий | Прибрати гілку необов'язкового телефону, узгодити з формою | Запит без телефону отримує 400 |
| Маршрути (`collaboration`, `contact`) | змінені | середній | Прийняти файл, обрати, який маршрут лишається | Завеликий файл відхиляється |
| Сервіс пошти (`emailService.ts`) | нова робота | високий | Зараз не викликається: треба підключити й додати вкладення | Лист містить телефон і посилання |
| Сервіс завантаження (`upload.ts`) | змінений | високий | Зараз демо-заглушка; визначити сховище | Завантажений PDF відкривається |
| Тести (`ContactForm.test.tsx`, `validateContactData.test.ts`) | змінені | середній | Оновити очікування | Усі тести проходять |
| Переклади (`i18n/messages`) | змінені | низький | Тексти помилок телефону, файлу (uk і en) | Показується правильна мова |
| Конфігурація | нова | середній | Ліміти розміру й типу файлу в константах | Межі беруться з однієї константи |

## 4. Тіло issue після уточнення (критерії приймання)

Використайте розділ 5 із `contact-form-feature.md` (Given/When/Then).

## 5. Коментар «Open questions for the stakeholder:»

Використайте розділ 7 із `contact-form-feature.md` (10 питань).
