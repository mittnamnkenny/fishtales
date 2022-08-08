from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs['placeholder'] = 'Add comment...'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'location',
            'fish_caught',
            'weather_conditions',
            'featured_image',
            'content'
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
