from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     context = {'posts':posts}
#     return render(request, 'blog/post_list.html', context)

# def detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     context= {'object':post, 'post':post}
#     return render(request, 'blog/post_detail.html', context)

