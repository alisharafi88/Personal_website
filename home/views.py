from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import AboutMe
from resumes.models import CourseCategory, SkillCategory
from portfolio.models import Portfolio
from testimonials.models import Comment
from blogs.models import Blog


class HomeView(View):
    def get(self, request):
        about_me = get_object_or_404(AboutMe, pk=1)

        course_category_queryset = CourseCategory.course_exist.all()
        skill_category_queryset = SkillCategory.skill_exist.all()

        portfolio_queryset = Portfolio.objects.all()

        comment_queryset = Comment.objects.filter(is_active=True)

        blog_queryset = Blog.objects.filter(is_active=True)
        return render(
            request,
            '-base.html',
            {
                'about_me': about_me,
                'course_categories': course_category_queryset,
                'skill_categories': skill_category_queryset,
                'portfolios': portfolio_queryset,
                'comments': comment_queryset,
                'blogs': blog_queryset,
            }
        )
