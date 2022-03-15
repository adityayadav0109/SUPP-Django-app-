import email
from msilib.schema import Class
from django.db import models

# Create your models here.
class Feedback (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField()
    description = models.TextField()
    
