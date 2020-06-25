from django.contrib import admin
from .models import Download



class DownloadAdmin(admin.ModelAdmin):
    list_display = ('name','description')


admin.site.register(Download,DownloadAdmin)
