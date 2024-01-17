from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'user_is_connected', 'created_at', 'updated_at', 'user_is_deleted')
    search_fields=('id', 'username', 'email')
    list_filter=('id', 'username', 'email', 'created_at', 'updated_at')


