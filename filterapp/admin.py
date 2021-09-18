# Import admin module
from django.contrib import admin
# Import Employee model
from .models import Employee

# Register employee model
admin.site.register(Employee)