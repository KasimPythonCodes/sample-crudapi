from django.db import models

# Create your models here.

class Student(models.Model):
    email = models.EmailField(max_length=150)
    Password = models.CharField(max_length=150)
    
    def __str__(self):
        return self.email
    