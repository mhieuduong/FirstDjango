from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {
        'slug': ('title',)}  # prepopulated the `slug` field
    # with the input of title
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    oredering = ('status', 'publish')
