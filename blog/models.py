from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify


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


def default_title():
    """Set deafaul Post title"""
    return str(f'Fishing {datetime.today()}')[:24]


class Post(models.Model):
    """
    Database model for Posts
    """
    title = models.CharField(
        max_length=200, unique=True,
        default=default_title
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
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """Set the order of posts by date descending"""
        ordering = ['-created_on']

    def __str__(self):
        """Returns a string representation of an object"""
        return self.title

    def number_of_likes(self):
        """Returns number of blog post likes"""
        return self.likes.count()

    def get_absolute_url(self):
        """Returns successful post to related slug url"""
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Save method override with slugify"""
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Database model for comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """Sets the order of comments by date ascending"""
        ordering = ['created_on']

    def __str__(self):
        """Returns comment with body and name"""
        return f'Comment {self.body} by {self.author}'
