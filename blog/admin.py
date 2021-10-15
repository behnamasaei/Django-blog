from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # prepopulated slug field autoamte by title
    prepopulated_fields = {'slug': ('title',)}
    row_id_fields = ('author',)
    # sort navigation by publish
    date_hierarchy = 'publish'
    list_display_links = None


ordering = ('status', 'publish')
