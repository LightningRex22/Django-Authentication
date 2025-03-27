from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=50, default=None)
    def __str__(self):
        return self.department

class Degree(models.Model):
    degree = models.CharField(max_length=20, default=None)
    def __str__(self):
        return self.degree


class MyUser(AbstractUser):
    USER_TYPES=[
        ('',''),
    ]
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True, blank=True, default=None)
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']