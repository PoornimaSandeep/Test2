from django import forms
from .models import Profile


class EventsForm(forms.Form):
      class Meta:
            model=Profile()
            fields="__all__"
