from django import forms
from .models import student,staff


class staff_form(forms.ModelForm):
    class Meta:
          model=staff
          fields="__all__"

class student_form(forms.ModelForm):
    class Meta:
          model=student
          fields="__all__"