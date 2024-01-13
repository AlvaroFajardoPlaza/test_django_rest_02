from django.contrib import admin
from .models import TestModel01

@admin.register(TestModel01)
class TestModel01Admin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'description',
                    'image',
                    'url',
                    'created_at',
                    'updated_at',)
    search_fields=('id', 'name', 'description')
    list_filter=('id', 'name', 'image', 'created_at', 'updated_at')
