# FastAPI Service Base Template

## Подготовка к запуску

Рекомендованная версия Python: 3.11+

### Подготовка виртуального окружения

Для начала необходимо создать виртуальное окружение:

#### Windows | Linux
```shell
python -m venv venv
```

#### macOS
```shell
python3 -m venv venv
```

Активируем созданное окружение:

##### Windows
```shell
venv\Scripts\Activate.ps1
```

#### macOS | Linux
```shell
source venv/bin/activate
```

Установим зависимости:

```shell
pip install -r requirements.dev.txt
```

### Что насчет БД?

Используемая БД: PostgreSQL

Для поднятия БД необходимо предварительно установить Docker (включая модули docker-compose)

```shell
docker-compose up -f docker-compose.dev.yml.up -d
```

## Запуск

Поднимем наш сервис:

```shell
uvicorn app:app --reload
```

## Мигрируем?

Для генерации миграций используется alembic:

```bash
alembic revision --autogenerate -m "init"
```

Миграция существующей БД:

```bash
alembic upgrade head
```
