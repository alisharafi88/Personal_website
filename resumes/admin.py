from django.contrib import admin

from .models import Course, Skill, CourseCategory, SkillsCategory


@admin.register(CourseCategory)
class CategoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(SkillsCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)
