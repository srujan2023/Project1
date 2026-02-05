from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=11,unique=True)
    email=models.EmailField(unique=True)
    phone=models.BigIntegerField(unique=True)
    college=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    sem=models.IntegerField()
    
    def __str__(self):
     return self.name
    