from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['subject', 'updated_on', 'is_active']

