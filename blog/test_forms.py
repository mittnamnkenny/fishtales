from django.test import TestCase
from .forms import CommentForm, PostForm


class TestCommentForm(TestCase):
    """
    Test fields on comment form
    """
    def test_comment_body_is_required(self):
        """Test that body field is required"""
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_comment_metaclass(self):
        """Test body field is explicit in comment metaclass"""
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestPostForm(TestCase):
    """
    Test fields on post form
    """
    def test_post_title_is_required(self):
        """Test that title field is required"""
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_location_is_required(self):
        """Test that location field is required"""
        form = PostForm({'location': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('location', form.errors.keys())
        self.assertEqual(form.errors['location'][0], 'This field is required.')

    def test_post_fish_caught_is_required(self):
        """Test that fish_caught field is required"""
        form = PostForm({'fish_caught': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('fish_caught', form.errors.keys())
        self.assertEqual(form.errors['fish_caught'][0],
                         'This field is required.')

    def test_post_weather_conditions_is_required(self):
        """Test that weather_conditions field is required"""
        form = PostForm({'weather_conditions': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('weather_conditions', form.errors.keys())
        self.assertEqual(form.errors['weather_conditions'][0],
                         'This field is required.')

    def test_post_content_is_required(self):
        """Test that content field is required"""
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_post_metaclass(self):
        """Test fields are explicit in post metaclass"""
        form = PostForm()
        self.assertEqual(form.Meta.fields, ['title', 'location', 'fish_caught',
                         'weather_conditions', 'featured_image', 'content'])
