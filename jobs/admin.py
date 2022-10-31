from django.contrib import admin
from .models import Job, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "created"]
    search_fields = ["name"]
    date_hierarchy = "created"
    readonly_fields = ("updated", "created")
    ordering = ["created"]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "postedby", "created"]
    search_fields = ["company", "title"]
    date_hierarchy = "updated"
    readonly_fields = ("created", "updated")
    ordering = ["updated"]
