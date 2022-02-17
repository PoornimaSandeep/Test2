from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class Profile(models.Model):
    email = models.CharField(max_length=150)
    username = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
    Firstname = models.CharField(max_length=150)
    Lastname = models.TextField()
    def __str__(self):
        return self.username