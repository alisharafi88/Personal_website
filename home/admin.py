from django.contrib import admin


from .models import AboutMe, File


class FileInline(admin.TabularInline):
    model = File
    extra = 1


@admin.register(AboutMe)
class MeAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')
    inlines = (FileInline, )
