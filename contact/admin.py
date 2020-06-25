from django.contrib import admin
from.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')

admin.site.register(Contact, ContactAdmin)




