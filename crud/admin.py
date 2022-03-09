from django.contrib import admin
from .models import Posts
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content')
    search_fields = ('title', 'slug', 'content')

admin.site.register(Posts, PostsAdmin)