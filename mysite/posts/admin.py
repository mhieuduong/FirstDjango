from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    list_display = ['title', 'created_at', 'updated_at']
    ordering = ['title', 'created_at']
    search_fields = ['title']



admin.site.register(Post, PostAdmin)