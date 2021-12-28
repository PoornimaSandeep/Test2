from django.contrib import admin
from .models import customuser,Admin,Staff,Student,Course,Subject,Attendence,AttendenceReport,LeaveReportStudent,LeaveReportStaff,FeedBackReportStudent
from .models import FeedBackReportStaff,NotificationStudent,NotificationStaff
from django.contrib.auth.admin import UserAdmin




# Register your models here.
class UserModel(UserAdmin):
      list_filter = ('user_type','first_name','last_name')



admin.site.register(Admin,UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Attendence)
admin.site.register(AttendenceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackReportStudent)
admin.site.register(FeedBackReportStaff)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaff)
