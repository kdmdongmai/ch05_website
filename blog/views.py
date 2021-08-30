from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'post':post})