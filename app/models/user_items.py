from __future__ import annotations
from tortoise import fields, models


class User(models.Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=30, unique=True)
    email = fields.CharField(max_length=50, unique=True)
    nickname = fields.CharField(max_length=30)
    hashed_password = fields.CharField(max_length=200)
    is_verified = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    registered_at = fields.DatetimeField(auto_now=True)

    todos: fields.ReverseRelation[Todo]


class Todo(models.Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=200)
    is_done = fields.BooleanField(default=False)

    creator: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="todos", on_delete=fields.CASCADE
    )




