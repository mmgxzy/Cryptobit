from django.urls import path
from apps.base.views import index, about, roadmap

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name="about"),
    path('roadmap/', roadmap, name="roadmap"),
]
