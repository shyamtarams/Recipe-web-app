from django import forms
from .models import Upload

class PostForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ['title', 'cover']