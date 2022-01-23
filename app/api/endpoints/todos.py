from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from app import schemas, models
from app.core.dependancies import get_current_user

router = APIRouter(
    responses={
        401: {}, 403: {}, 404: {},
    }
)


async def get_updateable_todo(
        todo_id: UUID,
        current_user: models.User = Depends(get_current_user)
) -> models.Todo:
    todo = await models.Todo.get(id=todo_id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    creator = await todo.creator
    if creator.id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Can only update todos created by user"
        )
    return todo


@router.post("/", response_model=schemas.Todo, status_code=201)
async def create_todo(
        todo: schemas.TodoCreate,
        current_user: models.User = Depends(get_current_user)
):
    return await models.Todo.create(**todo.dict(), creator_id=current_user.id)


@router.put("/{todo_id}", response_model=schemas.Todo)
async def update_todo(
        todo: schemas.TodoUpdate,
        prev_todo: models.Todo = Depends(get_updateable_todo)
):
    await prev_todo.update_from_dict(
        todo.dict(exclude_unset=True)
    )
    await prev_todo.save()
    return prev_todo


@router.delete("/{todo_id}", response_model=None, status_code=204)
async def update_todo(
        prev_todo: models.Todo = Depends(get_updateable_todo)
):
    await prev_todo.delete()
