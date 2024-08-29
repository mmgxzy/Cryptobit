from django.contrib import admin

from apps.blog.models import Blog, Story, Experts

admin.site.register(Blog)
admin.site.register(Story)
admin.site.register(Experts)