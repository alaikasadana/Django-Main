from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    age=models.IntegerField()
    contact=models.IntegerField()
  

