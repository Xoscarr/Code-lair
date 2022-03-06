from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post 


class PostListView(ListView):
    template_name = "post/detail.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post 


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields =['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.User
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     template_name = "post/edit.html"
     model = Post
     fields = ["title", "body"]

     def test_func(self):
         obj = self.get_object()
         return obj.author == self.request.User

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 


