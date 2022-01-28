from tortoise import fields, models

from .user import User


class Todo(models.Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=200)
    due_date = fields.DateField()
    is_done = fields.BooleanField(default=False)

    creator: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="todos", on_delete=fields.CASCADE
    )
