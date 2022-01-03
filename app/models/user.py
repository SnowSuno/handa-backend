from tortoise import fields, models

class User(models.Model):
    uuid = fields.UUIDField(pk=True)
    id = fields.CharField(max_length=30)
    email = fields.CharField(max_length=50)
    nickname = fields.CharField(max_length=30)
    hashed_password = fields.CharField(max_length=200)
    is_verified = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    registered_at = fields.DatetimeField(auto_now=True)
