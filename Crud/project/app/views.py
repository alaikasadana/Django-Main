
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'list.html', {'posts': posts})


def add_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'add.html')


def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list')

    return render(request, 'update.html', {'post': post})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')