from django.shortcuts import render
from django.views.generic import ListView
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


def about(request):
    return render(request, 'blog_app/about.html', {'title':'About Page'})
