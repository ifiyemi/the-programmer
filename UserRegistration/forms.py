__author__ = 'IFIYEMI'


from django import forms
from .models import RegDetails

class PostForm(forms.ModelForm):
  class Meta:
    model = RegDetails
    fields = ('name', 'mail_address')