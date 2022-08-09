from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    Form for comments
    """
    class Meta:
        """Form fields"""
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        """Remove body label and add placeholder text"""
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs['placeholder'] = 'Add comment...'


class PostForm(forms.ModelForm):
    """
    Form for posts
    """
    class Meta:
        """Form fields"""
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
