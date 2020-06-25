from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('post_num','date')

admin.site.register(Blog, BlogAdmin)




