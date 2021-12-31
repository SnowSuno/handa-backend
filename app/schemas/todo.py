from app.models.todo import TodoModel
from tortoise.contrib.pydantic import pydantic_model_creator

Todo = pydantic_model_creator(TodoModel)
