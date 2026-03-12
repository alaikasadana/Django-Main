from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField(null=True)
    qualification = models.CharField(max_length=100)
    state=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    document = models.FileField(upload_to='documents')
    audio = models.FileField(upload_to='audio')
    video = models.FileField(upload_to='videos')
    
    def __str__(self):
        return self.name + " " + self.email + " " + str(self.contact)
    
