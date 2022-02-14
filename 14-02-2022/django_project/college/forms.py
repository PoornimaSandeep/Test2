from django import forms
from .models import college_model

class college_form(forms.ModelForm):
    class Meta:
          model=college_model
          fields="__all__"