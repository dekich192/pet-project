from sqlalchemy import Column, Integer, String, Table, MetaData
from databasa import Base
from sqlalchemy.orm import Mapped, mapped_column



class workers(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)  #декларотивный стиль
    username: Mapped[str] = mapped_column(String(20))
    