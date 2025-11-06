from sqlalchemy import text, insert
from sqlalchemy.orm import session
from databasa import sync_engine, async_engine, session_factory
from models import metadata_obj, workers, WorkersOrm



def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True
                                                        #синхронное создание таблицы
    
def insert_data():
    worker_bobr = WorkersOrm(username="bobr")
    worker_volk = WorkersOrm(username="volk")
    session.add_all([worker_bobr, worker_volk])
    session.commit()