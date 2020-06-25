from django.contrib import admin
from .models import YourBlog


class YblogAdmin(admin.ModelAdmin):
    list_display = ('name', 'dt')

admin.site.register(YourBlog, YblogAdmin)
