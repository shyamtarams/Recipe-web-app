from django import forms
from .models import Post



class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title']
        widgets = {
             'publish_date': DateInput(),
         }



'''class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)'''