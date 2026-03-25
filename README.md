[![CI](https://github.com/paalso/shop_hopper/actions/workflows/ci.yml/badge.svg)](https://github.com/paalso/shop_hopper/actions/workflows/ci.yml)

# 🛍️ Shop Hopper

**Shop Hopper** - консольная утилита для поиска товаров на различных торговых площадках. Реализовано для поиска на основных украинских сайтах, предлагающих букинистическую продукцию. Может быть адаптировано для других целей. Позволяет выполнять поиск по ключевым словам, выбирать платформы, исключать ненужные и сохранять результаты в удобных форматах (HTML или JSON).

## 📦 Возможности

- 🔍 Поиск по ключевым словам на нескольких платформах
- ✅ Выбор/исключение платформ
- 📄 Сохранение в HTML и JSON
- 🌐 Открытие HTML-файла в браузере
- 🎨 Красивый терминальный вывод с [rich](https://github.com/Textualize/rich)

## 🚀 Быстрый старт

### 📥 Установка для пользователя через pipx

```
pipx install git+https://github.com/paalso/shop_hopper.git
```

[![asciicast](https://asciinema.org/a/7SI7dVJ05K2ISqcq7pvVzR7F1.svg)](https://asciinema.org/a/7SI7dVJ05K2ISqcq7pvVzR7F1)


### 🛠️ Установка для разработчиков
```
git clone https://github.com/your-username/shop_hopper.git
cd shop_hopper
make install
cp .env_copy .env
```

## 🧑‍💻 Использование

```
shop-hopper "чалий сто пригод барвінка" -p olx alib --json
```

### Аргументы CLI
| Аргумент                | Описание                                               |
| ----------------------- | ------------------------------------------------------ |
| `запрос`                | Поисковый запрос (например, название книги)            |
| `-o`, `--output-dir`    | Каталог для сохранения результатов                     |
| `-p`, `--platforms`     | Перечень платформ, через пробел (например: `olx alib`) |
| `-i`, `--ignored`       | Платформы, которые следует исключить                   |
| `--json`                | Сохранить результат также в JSON                       |
| `--html` (по умолчанию) | Сохранить в HTML                                       |
| `--open`                | Открыть HTML-файл в браузере                           |

[![asciicast](https://asciinema.org/a/FmcoymVX0ePRSQKQpcyJYXNh6.svg)](https://asciinema.org/a/FmcoymVX0ePRSQKQpcyJYXNh6)


## 🧱 Используемый стек

- Python 3.11+

- Poetry - управление зависимостями

- BeautifulSoup - HTML-парсинг

- Requests - HTTP-запросы

- Jinja2 - генерация HTML-отчёта

- Rich - красивый вывод в терминале

- Selenium - (опционально) загрузка динамического контента

  ## TODO:

- Какая-то [аварийная ситуция осталась необработанной](https://github.com/paalso/shop_hopper/blob/master/bug_to_fix.txt) - устранить

- Изменить логику формирования запросов с последовательной на асинхронную с [asyncio](https://docs.python.org/3.14/library/asyncio.html)

- Добавить парсер для [shafa.ua](https://shafa.ua)

- Докеризовать

- Попробовать запилить сервис, который бы сохранял результаты в БД, осуществлял регулярный поиск по расписанию, уведомлял о новых поступлениях
