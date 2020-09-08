from django.db import models

# Create your models here.
class info(models.Model):
    g=(('MALE',"MALE"),('FEMALE','FEMALE'))
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6,choices=g)
    dob=models.CharField(max_length=6)
    branch=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
