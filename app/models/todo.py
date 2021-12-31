from tortoise import fields, models

class TodoModel(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)

