from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'photo')
    search_fields = ('user', 'first_name', 'last_name', 'email')
    list_filter = ('created_date',)