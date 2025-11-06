import  asyncio
from curses import echo
from sqlalchemy import create_engine
from config1 import settings
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


sync_sessionmaker = sessionmaker(
    url=settings.database_url_psycopg,
    echo=True
)

async_sessionmaker = async_sessionmaker(
    url=settings.database_url_asyncpg,
    echo=False
)

sync_engine = create_engine(settings.database_url)
async_engine = create_async_engine(settings.database_url)


class Base(DeclarativeBase):
    pass

