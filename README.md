# Autotest PostgreSQL Docker

Проект содержит автотесты для проверки подключения к базе данных и выполнения простейшего запроса: `SELECT now()`. Оформлен с использованием `pytest` и драйвера `psycopg` (версия 3), упакован в Docker-контейнер.

[![Python](https://img.shields.io/badge/python-3.14-blue)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-16-blue)](https://www.postgresql.org/)
[![Pytest](https://img.shields.io/badge/pytest-9.1-orange)](https://docs.pytest.org/)
[![Docker](https://img.shields.io/badge/docker-compose-blue)](https://www.docker.com/)

---

## Информация о проекте

| | |
|---|---|
| **Задача** | Проверка подключения к БД и выполнение запроса `SELECT now()` |
| **СУБД** | PostgreSQL 16 (в Docker) |
| **Порт хоста** | `5433` (проброшен на стандартный `5432` внутри контейнера) |
| **Пользователь** | `testuser` / `testpass` |
| **База данных** | `testdb` |

---

## Быстрый запуск

### Шаг 1. Поднять базу данных
Убедитесь, что Docker Desktop запущен, и выполните:

    docker compose up -d

Дождитесь статуса `(healthy)`. Проверить статус можно командой:

    docker compose ps

### Шаг 2. Установить зависимости
Установите нужные библиотеки и зависимости из файла:

    pip install -r requirements.txt

---

## Запуск тестов

### Успешный прогон
Проверяет, что соединение устанавливается (`db_conn.closed is False`), а запрос `SELECT now()` возвращает результат. Конфигурация подключения описана в `conftest.py`.

    pytest test_main.py -v

Ожидаемый результат: `2 passed`

### Демонстрация падения
Специальный тест, который намеренно использует неверный хост (`fake_localhost`), чтобы продемонстрировать падение при некорректных параметрах подключения.

    pytest test_will_fall.py -v

Ожидаемый результат: `1 failed` (с ошибкой `getaddrinfo failed` - хост не резолвится).

---

## Структура проекта

| Файл | Описание |
|---|---|
| `docker-compose.yml` | Конфигурация PostgreSQL 16 в Docker (проброс порта `5433 -> 5432`). |
| `conftest.py` | Фикстура `db_conn` для установки и закрытия соединения с БД. |
| `test_main.py` | Позитивные тесты (проверка статуса соединения и выполнение запроса). |
| `test_will_fall.py` | Негативный тест (демонстрация падения при неверном хосте). |
| `requirements.txt` | Список зависимостей проекта. |
| `.gitignore` | Исключения для Git (виртуальное окружение, кэш, системные файлы). |
