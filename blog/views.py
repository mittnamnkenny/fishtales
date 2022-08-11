from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm, PostForm


class RecentPostList(generic.ListView):
    """
    View for displaying 3 latest blog posts on home page,
    including filter by approved and order by date descending
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'index.html'


class PostList(generic.ListView):
    """
    View for displaying all blog posts on blog page,
    including filter by approved and order by date descending,
    paginated by 6 blog posts on each page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):
    """
    View for displaying individual blog posts on a single page,
    including features to add a comment or like
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Get method to retrieve post details including comments and likes
        and render post detail page
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method to validate comment input, save and re-load
        post detail page
        Success message as user feedback
        """
        if request.user.is_authenticated:
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, 'Comment Added')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(LoginRequiredMixin, View):
    """
    View to remove or add like on post detail page
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Post method to toggle post like and redirect
        to post detail page
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostAdd(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    View to allow users to add a new blog post
    Success message as user feedback
    """
    model = Post
    template_name = 'post_add.html'
    form_class = PostForm
    success_message = 'Post Added'

    def form_valid(self, form):
        """Validate form after connecting form author to user"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin,
                 SuccessMessageMixin,
                 UserPassesTestMixin,
                 generic.UpdateView):
    """
    View to allow users to update their blog post
    on the post detail page
    Success message as user feedback
    """
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm
    success_message = 'Post Updated'

    def form_valid(self, form):
        """Validate form after connecting form author to user"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Test that logged in user is post author"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDelete(LoginRequiredMixin,
                 SuccessMessageMixin,
                 UserPassesTestMixin,
                 generic.DeleteView):
    """
    View to allow users to delete their blog post
    on the post detail page
    Success message as user feedback
    """
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('blog')
    success_message = 'Post Deleted'

    def delete(self, request, *args, **kwargs):
        """Generate success message on delete view"""
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)

    def test_func(self):
        """Test that logged in user is post author"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentUpdate(LoginRequiredMixin,
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    generic.UpdateView):
    """
    View to allow users to update their comment
    on the post detail page
    Success message as user feedback
    """
    model = Comment
    template_name = 'comment_update.html'
    form_class = CommentForm
    success_message = 'Comment Updated'

    def get_success_url(self):
        """Success url for post associated with comment"""
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})

    def form_valid(self, form):
        """Validate form after connecting form author to user"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Test that logged in user is comment author"""
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDelete(LoginRequiredMixin,
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):
    """
    View to allow users to delete their comment
    on the post detail page
    Success message as user feedback
    """
    model = Comment
    template_name = 'post_detail.html'
    success_message = 'Comment Deleted'

    def get_success_url(self):
        """Success url for post associated with comment"""
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})

    def delete(self, request, *args, **kwargs):
        """Generate success message on delete viev"""
        messages.success(self.request, self.success_message)
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def test_func(self):
        """Test that logged in user is comment author"""
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
