from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import Post

def home(request):
    # grab data into a dictionary
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_app/home.html', context)


# List view to query Post model
class PostListView(ListView):
    model = Post

    # Set template to display
    template_name = 'blog_app/home.html'

    # Set variable containing posts
    context_object_name = 'posts'

    # Order date field from newest to oldest, by default its newest to oldest
    ordering = ['-date_posted']


# Detail view to query specicif Post 
class PostDetailView(DetailView):
    model = Post


# Create view to create a user post 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Validate form 
    def form_valid(self, form):
        # Set form author 
        form.instance.author = self.request.user

        # Validate form by running current method on parent class 
        return super().form_valid(form)


# Create view to update a user post 
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Validate form 
    def form_valid(self, form):
        # Set form author 
        form.instance.author = self.request.user

        # Validate form by running current method on parent class 
        return super().form_valid(form)
    
    # Test if user is the author of post
    def test_func(self):
        # Grab the post
        post = self.get_object()

        # Compare post attribute(author) and one making request(logged in user)
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog_app/about.html', {'title':'About Page'})
