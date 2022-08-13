from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestModels(TestCase):
    """
    Test blog app models
    """
    @classmethod
    def setUpTestData(self):
        """Create test data"""
        self.user = User.objects.create(username='testname')
        self.user.set_password('1234')
        self.user.save()

        self.post = Post.objects.create(
            title='test post',
            slug='test-post',
            author=self.user,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='test comment'
        )

    def test_post_model_str(self):
        """Test the __str__ method for post"""
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_absolute_url_str(self):
        """Test absolute_url for post"""
        self.assertEqual(self.post.get_absolute_url(), f'/{self.post.slug}/')

    def test_comment_model_str(self):
        """Test the __str__ method for comment"""
        self.assertEqual(
            self.comment.__str__(),
            f'Comment {self.comment.body} by {self.comment.author}'
            )

    def test_post_defaults(self):
        """Test default values"""
        self.assertTrue(self.post.location == 0)
        self.assertTrue(self.post.fish_caught == 0)
        self.assertTrue(self.post.weather_conditions == 0)
        self.assertTrue(self.post.status == 1)
        self.assertTrue(self.comment.approved)
