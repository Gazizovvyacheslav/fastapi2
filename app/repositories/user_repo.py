from app.models.user import Task
from sqlalchemy import select

class TaskRepository():

    @staticmethod
    async def create_task(session, title: str, description: str) -> Task:
        task = Task(title = title, description = description) 
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    @staticmethod
    async def get_task(session, id: int) -> Task | None:
        task = await session.get(Task, id)
        return task

    @staticmethod
    async def get_tasks(session) -> list:

        res = await session.execute(select(Task))
        res = [*res.scalars()]
        return res

    @staticmethod
    async def update_task(session, is_done: bool, id: int) -> Task | None:
        task = await TaskRepository.get_task(session, id = id)
        if task is not None:
            task.is_done = is_done
        else:
            return None
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    @staticmethod
    async def delete_task(session, id) -> bool:
        task = await TaskRepository.get_task(session, id = id)
        if task is not None:
            await session.delete(task)
            await session.commit()
            return True
        else:
            return False
