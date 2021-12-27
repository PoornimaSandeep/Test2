from django import forms
from .models import Post ,signup
class Post_form(forms.ModelForm):
    class Meta:
          model=Post
          fields="__all__"

class signup_form(forms.ModelForm):
    class Meta:
          model=signup
          fields="__all__"
