from fastapi import APIRouter, Depends, Response

from app.schemas.user import CreateTask
from app.repositories.user_repo import TaskRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db import get_session
from app.schemas.user import CreateTask, ReadTask, UpdateTask

from fastapi import HTTPException

router = APIRouter(prefix="/tasks")

@router.post("", status_code=201)
async def create_task(data: CreateTask, session: AsyncSession = Depends(get_session)) -> ReadTask:
    task = await TaskRepository.create_task(
        session=session, title=data.title, description=data.description
    )
    return task

@router.get("/{task_id}")
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)) -> ReadTask:
    task = await TaskRepository.get_task(
        session=session, id=task_id,
    )
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("")
async def get_tasks(session: AsyncSession = Depends(get_session)) -> list[ReadTask]:
    tasks = await TaskRepository.get_tasks(
        session=session
    )
    return tasks

@router.patch("/{task_id}")
async def update_task(data: UpdateTask, task_id: int, session: AsyncSession = Depends(get_session)) -> ReadTask:
    task = await TaskRepository.update_task(
        session=session, is_done=data.is_done, id=task_id,
    )
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)) -> Response:
    task = await TaskRepository.delete_task(
        session=session, id=task_id,
    )
    if task is False:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=204)
