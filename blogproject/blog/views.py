# from django.shortcuts import render
# from .models import Post
# def post_list(request):
#     posts=Post.objects.all()
#     return render(request,'blog.html',{'posts':posts})

# # Create your views here.
from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('postlist')

    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def postdelete(request,postid):
    post=Post.objects.get(id=postid)
    post.delete()
    return redirect('postlist')

    
