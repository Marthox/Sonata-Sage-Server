from django.db.models import AutoField, CharField, BooleanField, DateTimeField
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Disciple(AbstractBaseUser):
    id = AutoField(primary_key=True)
    username = CharField(max_length=100)
    mail = CharField(max_length=100)
    password = CharField(max_length=100)
    is_active = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
