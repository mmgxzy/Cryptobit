from django.urls import path
from apps.blog.views import blog, article, team, project, blog_details


urlpatterns = [
    path('blog/', blog, name="blog"),
    path('article/', article, name="article"),
    path('team/', team, name="team"),
    path('project/', project, name="project"),
    path('blog_details/<int:id>/', blog_details, name="blog_details"),
]