from envparse import env
from dotenv import load_dotenv

from sqlmodel import SQLModel

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

POSTGRES_HOST = env.str('POSTGRES_HOST')
POSTGRES_PORT = env.str('POSTGRES_PORT')
POSTGRES_DB = env.str('POSTGRES_DB')
POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')

DATABASE_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}' \
               f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def init_db():
    """
    Инициализация подключения к базе данных
    :return: None
    """
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# noinspection PyTypeChecker
async def get_session() -> AsyncSession:
    """
    Получение сессии подключения к БД
    :return: сессия
    """
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session
