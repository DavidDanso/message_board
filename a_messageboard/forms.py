from django import forms
from django.forms import ModelForm
from .models import *

class MessageCreationForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Post a message...', 'class': 'p-4 text--black', 'maxlength': '2000'}),
        }