from django.contrib import admin

# Register your models here.
from community.models import Like, Follow

admin.site.register(Like)
admin.site.register(Follow)