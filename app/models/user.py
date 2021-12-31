from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=30)
    hashed_password = fields.CharField(max_length=50)
    is_verified = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
