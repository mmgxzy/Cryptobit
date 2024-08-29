from django.shortcuts import render
from apps.blog.models import Blog, Story, Experts

def article(request):
    blog = Blog.objects.latest('id')
    story_all = Story.objects.all()
    return render(request, 'article.html', locals())

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', locals())

def team(request):
    expert_all = Experts.objects.all()
    blog = Blog.objects.latest('id')
    return render(request, 'team.html', locals())

def project(request):
    return render(request, 'project.html', locals())

def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog-details.html', locals())
