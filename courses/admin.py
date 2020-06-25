from django.contrib import admin
from.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name_of_channel', 'for_which_language')

admin.site.register(Course, CourseAdmin)


