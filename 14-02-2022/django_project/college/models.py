from django.db import models

# Create your models here.

class college_model(models.Model):
      stu_id=models.IntegerField(primary_key=True)
      name=models.CharField(max_length=100)
      Kannada=models.IntegerField()
      English = models.IntegerField()
      Hindhi = models.IntegerField()
      Maths = models.IntegerField()
      Science = models.IntegerField()
      Social = models.IntegerField()
      photo=models.ImageField(upload_to="images/")

      def __str__(self):
          return self.name
