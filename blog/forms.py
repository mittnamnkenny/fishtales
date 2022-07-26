from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


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
