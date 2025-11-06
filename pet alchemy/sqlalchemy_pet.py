from uuid import UUID
from sqlalchemy import Column, create_engine, text, column, Integer, String, MetaData       
from sqlalchemy.orm import sessionmaker                     
from config1 import settings
from corik import create_tables
from sqlalchemy import Table

create_tables()

engine = create_engine(
    url=settings.database_url,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION()"))
        version = result.fetchone()
        res = conn.execute(text("SELECT 1, 2, 3, union all select 4, 5, 6"))
        print(f"{res.first=}")
        print(f"PostgreSQL version: {version[0] if version else 'Unknown'}")#подключение к базе данных сырые запросы через engine
        print("Connection successful!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    print("Please check your .env file and database settings.")
    
    
    
metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", UUID, primary_key=True),      #таблица в базе данных (не созданная)
    Column("username")
)


    