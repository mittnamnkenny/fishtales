from .models import Comment, Post
from django import forms


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
