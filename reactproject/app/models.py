from django.db import models

# Create your models here.

class Task(models.Model):
    titile=models.TextField()
    dis=models.TextField()
