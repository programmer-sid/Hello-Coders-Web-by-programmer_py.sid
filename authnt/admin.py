from django.contrib import admin
from.models import Login


class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


admin.site.register(Login, LoginAdmin)
