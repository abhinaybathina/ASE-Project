from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Class based views are being used.
# Template Name = <app>/<model>_<viewtype>.html
class PostListView(LoginRequiredMixin, ListView):
    model = Post


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'Blog'
        context['title'] = title
        context['comments'] = Comment.objects.filter(post=context['post']).order_by('date_posted')
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'type', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image', 'type', 'title', 'content']
    success_url = '/user/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/user/blog/'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
