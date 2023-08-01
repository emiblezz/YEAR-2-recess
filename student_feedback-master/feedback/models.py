from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class User(models.Model):
    email_address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

