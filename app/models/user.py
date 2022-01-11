from tortoise import fields, models

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .todo import Todo

class User(models.Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=30, unique=True)
    email = fields.CharField(max_length=50, unique=True)
    nickname = fields.CharField(max_length=30)
    hashed_password = fields.CharField(max_length=200)
    is_verified = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    registered_at = fields.DatetimeField(auto_now=True)

    todos: fields.ReverseRelation["Todo"]

    def __str__(self):
        return self.username
