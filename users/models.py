from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomuserManager

# Create your models here.

class USER(AbstractUser):
    username  = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    adress = models.TextField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = CustomuserManager()

    def __str__(self):
        return self.email
    
