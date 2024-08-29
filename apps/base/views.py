from django.shortcuts import render
from apps.base.models import Settings, Image, Cryptobit, Experts, ExpertsFoto, Story, About, ProjectFoto, ArticlesFoto, Team

def index(request):
    settings_id = Settings.objects.latest('id')
    image_all = Image.objects.all()
    cryptobit = Cryptobit.objects.latest('id')
    experts = Experts.objects.latest('id')
    experts_foto = ExpertsFoto.objects.all()
    story_all = Story.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    image_all = Image.objects.all()
    about = About.objects.latest('id')
    image_project = ProjectFoto.objects.all()
    settings_id = Settings.objects.latest('id')
    articles_all = ArticlesFoto.objects.all()
    return render(request, 'about.html', locals())

def roadmap(request):
    settings_id = Settings.objects.latest('id')
    about = About.objects.latest('id')
    story_all = Story.objects.all()
    image_all = Image.objects.all()
    team= Team.objects.latest('id')
    return render(request, 'roadmap.html', locals())


# Create your views here.
