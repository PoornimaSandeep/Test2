from django.db import models

# Create your models here.
type=(
    ('Dose1','Dose1'),
    ('Dose2','Dose2')
)

class user_data(models.Model):
      adhar_no=models.IntegerField(primary_key=True)
      Mobile_no=models.IntegerField()
      name=models.CharField(max_length=300)
      dose=models.CharField(max_length=100,null=True)
      adhar_card=models.FileField(upload_to='images/',null=True)

      def __str__(self):
          return self.name
