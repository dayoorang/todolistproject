from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from projectapp.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['topic','image_tag','writer']
    list_display_links = ['topic']

    def image_tag(self,project):
        if project.image:
           return mark_safe(f'<img src="{project.image.url}" style="width: 72px"/>')
        return None