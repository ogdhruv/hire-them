from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "department", "date_joined")
    search_fields = ("email","first_name","last_name","roll_number")
    list_display_links = ["first_name"]
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  # this will make password in admin read only
    ordering = ["roll_number", "first_name"]
