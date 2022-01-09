from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class customuser(AbstractUser):
      user_type_data=(
      (1, 'HOD'),
      (2, 'Staff'),
      (3, 'Student'),

      )
      user_type=models.CharField(max_length=100,choices=user_type_data,default=1)



class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(customuser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(customuser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Course(models.Model):
      id=models.AutoField(primary_key=True)

      course_name=models.CharField(max_length=100)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now_add=True)
      objects=models.Manager()


class Subject(models.Model):
      id=models.AutoField(primary_key=True)

      subject_name=models.CharField(max_length=100)
      course_id=models.ForeignKey(Course,on_delete=models.CASCADE,)
      staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now_add=True)
      objects=models.Manager()




class Student(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(customuser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    profile_pic=models.ImageField(max_length=100)
    address=models.TextField()
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_start_year=models.DateField(null=True)
    session_end_year=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Attendence(models.Model):
    id=models.AutoField(primary_key=True)

    subject_id=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class AttendenceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendence,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=100)
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=100)
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class FeedBackReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class FeedBackReportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class NotificationStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    messages=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class NotificationStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    messages=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


@receiver(post_save,sender=customuser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
       if instance.user_type==1:
          Admin.objects.create(Admin=instance)
       if instance.user_type==2:
          staff.objects.create(admin=instance)
       if instance.user_type==3:
          student.objects.create(admin=instance)

@receiver(post_save,sender=customuser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
       if instance.user_type==1:
          instance.Admin.save()
       if instance.user_type==2:
          instance.staff.save()
          if instance.user_type==3:
             instance.student.save()

