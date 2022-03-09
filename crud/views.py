from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from django.contrib import messages
from .models import Posts


def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {
        'posts': posts
    })

def create(request):
    if request.POST:
        req = request.POST
        post = Posts(title=req.get('title'), slug=slugify(req.get('title')), content=req.get('content'))
        post.save()
        messages.success(request, 'The record was saved successfully')
        return redirect('/')
    else:
        return render(request, 'create.html')

def update(request, post_id):
    

    if request.POST:
        req = request.POST
        post = Posts.objects.get(id=post_id)
        post.title = req.get('title')
        post.slug = slugify(req.get('title'))
        post.content = req.get('content')
        post.save()
        messages.success(request, 'The record was saved successfully')
        return redirect('/')
    else:
        post = Posts.objects.get(id=post_id)
        return render(request, 'update.html', {
            'id': post.id,
            'title': post.title,
            'slug': post.slug,
            'content': post.content
        })

def read(request, post_slug):
    post = Posts.objects.get(slug=post_slug)
    return render(request, 'detail.html', {
        'id': post.id,
        'title': post.title,
        'slug': post.slug,
        'content': post.content
    })

def delete(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'The record was deleted successfully')
    return redirect('/')
