from django.db import models
dept = (
    (1,"CSE"),
    (2,"ISE"),
    (3,"ECE"),
    (4,"CIVIL"),
    (5,"MECH")
)

# Create your models here.
class staff(models.Model):
     emp_id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length=100, null=False)
     dept = models.IntegerField(choices=dept,default=1)

     def __str__(self):
        return self.name


class student(models.Model):
      usn=models.IntegerField(primary_key=True)
      name=models.CharField(max_length=100,null=False)
      dept=models.CharField(max_length=100,null=False)

      def __str__(self):
          return self.name
