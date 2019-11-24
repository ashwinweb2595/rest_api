from django.contrib import admin
from . models import employees

# Registering Model to add a Replica on Admin to CRUD
admin.site.register(employees)

