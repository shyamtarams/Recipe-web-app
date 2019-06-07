from django import forms
from posts.models import Post



class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'cover',  'description', 'publish_date']
        widgets = {
            'publish_date': DateInput(),
        }


from .models import Comment

class PostComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

