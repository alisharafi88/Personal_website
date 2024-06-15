from django.contrib import admin


from .models import AboutMe


@admin.register(AboutMe)
class MeAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')
