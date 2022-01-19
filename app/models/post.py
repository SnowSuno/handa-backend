from tortoise import fields, models

from .user import User

class AbstractPost(models.Model):
    class Meta:
        abstract = True

    id = fields.UUIDField(pk=True)
    content = fields.TextField()

    author: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="posts", on_delete=fields.SET_NULL
    )

    def __str__(self):
        return f"{self.content[:10]}..."

class TodoPost(AbstractPost):
    pass

class CompletePost(AbstractPost):
    pass
