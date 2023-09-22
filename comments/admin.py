from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on', 'is_active']
    ordering = ['created_on', 'is_active']
    fieldsets = (
        ('user', {'fields': ('user',)}),
        ('comment', {'fields': ('comment', 'is_active')}),
    )

