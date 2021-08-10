from django.contrib import admin

from project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "link"
    )
    list_display_links = ("name",)
    list_per_page = 20
    search_fields = ("name",)
