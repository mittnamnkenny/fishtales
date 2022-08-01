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
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'index.html'


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
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

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment Added')
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm(),
                'liked': liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostAdd(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):

    model = Post
    template_name = 'post_add.html'
    form_class = PostForm
    success_message = 'Post Added'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin,
                 SuccessMessageMixin,
                 UserPassesTestMixin,
                 generic.UpdateView):

    model = Post
    template_name = 'post_update.html'
    form_class = PostForm
    success_message = 'Post Updated'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDelete(LoginRequiredMixin,
                 SuccessMessageMixin,
                 UserPassesTestMixin,
                 generic.DeleteView):

    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('blog')
    success_message = 'Post Deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentDelete(LoginRequiredMixin,
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):

    model = Comment
    template_name = 'post_detail.html'
    success_message = 'Comment Deleted'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
