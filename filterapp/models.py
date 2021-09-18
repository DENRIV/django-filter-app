# Import models module
from django.db import models

# Define class to create employees table
class Employee(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=40)
    email = models.EmailField()
    department = models.CharField(max_length=30)
    joinning_date = models.DateField()