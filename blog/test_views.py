from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment


class TestViews(TestCase):
    """
    Test blog app views
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

    def test_get_recent_post_list(self):
        """Test home retrieval and correct template used"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_post_list(self):
        """Test blog retrieval and correct template used"""
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html', 'base.html')

    def test_get_post_detail(self):
        """Test post_detail retrieval and correct template used"""
        response = self.client.get(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    def test_get_post_add(self):
        """Test post_add retrieval and correct template used"""
        self.client.login(username='testname', password='1234')
        response = self.client.get('/post/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_add.html', 'base.html')

    def test_get_post_update(self):
        """Test post_update retrieval and correct template used"""
        self.client.login(username='testname', password='1234')
        response = self.client.get(
            reverse('post_update', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_update.html', 'base.html')

    def test_get_post_delete(self):
        """Test post_delete retrieval and correct template used"""
        self.client.login(username='testname', password='1234')
        response = self.client.get(
            reverse('post_delete', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    def test_post_comment(self):
        """Test post commenting feature"""
        self.client.login(username='testname', password='1234')
        response = self.client.post(
                    reverse('post_detail',
                            args=[self.post.slug]),
                    data={'body': 'testcomment'})
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))

    def test_post_like(self):
        """Test post like feature"""
        self.client.login(username='testname', password='1234')
        likes = self.post.likes.count()
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), likes+1)
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), likes)
