from django.db import models

# Create your models here.

class products(models.Model):
      name=models.CharField(max_length=1002,null=True)
      image=models.ImageField(upload_to="media/images",null=True)
      price=models.IntegerField(null=True)

