from django.contrib import admin
from .models import Room

# Register your models here.
@admin.register(Room)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "updated", "created"]
    search_fields = ["title", "description"]
    # raw_id_fields = ["host"]
    date_hierarchy = "created"
    ordering = ["created", "updated"]
