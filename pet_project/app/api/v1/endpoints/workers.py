from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ....database import get_async_db
from ....models.user import Worker
from ....schemas.user import WorkerCreate, WorkerResponse

router = APIRouter()

@router.post("/workers/", response_model=WorkerResponse)
async def create_worker(
    worker: WorkerCreate,
    db: AsyncSession = Depends(get_async_db)
):
    db_worker = Worker(username=worker.username)
    db.add(db_worker)
    await db.commit()
    await db.refresh(db_worker)
    return db_worker

@router.get("/workers/", response_model=List[WorkerResponse])
async def read_workers(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_db)
):
    result = await db.execute(
        select(Worker).offset(skip).limit(limit)
    )
    return result.scalars().all()

@router.get("/workers/{worker_id}", response_model=WorkerResponse)
async def read_worker(
    worker_id: str,
    db: AsyncSession = Depends(get_async_db)
):
    result = await db.execute(
        select(Worker).where(Worker.id == worker_id)
    )
    db_worker = result.scalars().first()
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker
