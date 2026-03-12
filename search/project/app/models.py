from django.db import models

# Create your models here.


class QueryData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    query = models.TextField()

    def __str__(self):
        return self.name
