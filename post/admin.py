from django.contrib import admin
from post.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'lead')
    list_filter = ('created_date', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('created_date',)
    prepopulated_fields = {'slug': ('title',)}