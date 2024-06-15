from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import AboutMe
from resumes.models import CourseCategory, SkillCategory


class HomeView(View):
    def get(self, request):
        about_me = get_object_or_404(AboutMe, pk=1)

        course_category_queryset = CourseCategory.course_exist.all()
        skill_category_queryset = SkillCategory.skill_exist.all()
        return render(request, '-base.html', {'about_me': about_me, 'course_category': course_category_queryset, 'skill_category': skill_category_queryset})

