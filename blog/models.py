from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

LOCATIONS = (
    (0, 'Alsterån'),
    (1, 'Hällesjön'),
    (2, 'Isgölen'),
    (3, 'Other')
)

WEATHER = (
    (0, '...'),
    (1, 'Sunny'),
    (2, 'Cloudy'),
    (3, 'Windy'),
    (4, 'Rainy'),
    (5, 'Snowy')
)


class Post(models.Model):
    title = models.CharField(
        max_length=200, unique=True,
        default=str(f'Fishing {datetime.today()}')[:24]
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    location = models.IntegerField(choices=LOCATIONS, default=0)
    fish_caught = models.IntegerField(default=0)
    weather_conditions = models.IntegerField(choices=WEATHER, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.author}'
