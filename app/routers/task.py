from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTaskc
from sqlalchemy import insert, select, update, delete
from slugify import slugify

task_router = APIRouter(prefix="/task", tags=["task"])


@task_router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task)).all()
    return task


@task_router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    try:
        task = db.scalars(select(Task).where(Task.id == task_id))
        return task
    except IndexError:
        raise HTTPException(status_code=404, detail='Message Not found')


@task_router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task_: CreateTask, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(insert(Task).values(
        title=create_task_.title,
        content=create_task_.content,
        priority=create_task_.priority,
        user_id=user_id,
        slug=slugify(create_task_.title)
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@task_router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTaskc):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    db.execute(update(Task).where(Task.id == task_id).values(firstname=update_task.firstname,
                                                             lastname=update_task.lastname,
                                                             age=update_task.age,
                                                             ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@task_router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    user = db.scalars(select(Task).where(Task.id == task_id))
    if user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User was deleted successful!'}