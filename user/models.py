from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    user_id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password', 'user_type']
    def __st__(self):
        return self.username
   