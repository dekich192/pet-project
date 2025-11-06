from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from ..config.settings import get_settings

settings = get_settings()

# Synchronous engine for migrations and sync operations
engine = create_engine(
    settings.database_url,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

# Async engine for async operations
async_engine = create_async_engine(
    settings.database_url.replace("postgresql", "postgresql+asyncpg"),
    echo=True,
)

# Session factories
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Base class for all models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Async dependency to get async DB session
async def get_async_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
