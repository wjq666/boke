
from django.contrib import admin
from blogs.apps.system.models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)