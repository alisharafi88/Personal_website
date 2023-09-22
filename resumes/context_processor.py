from .models import Skill, Course


def resume(request):
    skills = Skill.objects.all()
    skill_category = []
    for skill in skills:
        skill_category.append(skill.category.title_i18n)

    courses = Course.objects.all()
    course_category = []
    for course in courses:
        course_category.append(course.category.title_i18n)

    return {'skills': skills, 'courses': courses, 'skill_category': set(skill_category), 'course_category': set(course_category)}
