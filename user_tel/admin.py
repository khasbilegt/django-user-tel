from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    date_hierarchy = "date_joined"
    list_display = ("tel", "name", "date_joined", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser", "date_joined", "groups")
    fieldsets = (
        (None, {"fields": ("name", "tel", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("date_joined", "last_login")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("name", "tel", "password1", "password2")}),)
    readonly_fields = ("date_joined", "last_login")
    search_fields = ("tel", "name")
    ordering = ("-date_joined",)
