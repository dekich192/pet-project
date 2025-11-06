from sqlalchemy import text
from database import sync_engine, async_engine
from models import metadata_obj

def get_123_async():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.first()=}")
        
    
def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    
def insert_data():
    with sync_engine.connect() as conn:
        stmt = text("INSERT INTO workers (id, username) VALUES ('1', 'worker1'), ('2', 'worker2')")
        conn.execute(stmt)
        conn.commit()