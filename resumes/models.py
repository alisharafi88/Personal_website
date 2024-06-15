from django.db import models

from django.contrib.postgres.indexes import GinIndex
from django.utils.translation import gettext as _
from modeltrans.fields import TranslationField
from modeltrans.manager import MultilingualManager
from ckeditor.fields import RichTextField

from home.models import AboutMe


class CourseRelatedExistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('courses') \
            .filter(courses__isnull=False)


class CourseCategory(models.Model):
    title = models.CharField(_('Title'), max_length=20)
    body = RichTextField(_('Text'), blank=True, null=True)

    created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

    objects = MultilingualManager()
    course_exist = CourseRelatedExistManager()

    i18n = TranslationField(fields=('title', 'body'))

    class Meta:
        indexes = [GinIndex(fields=["i18n"])]
        verbose_name = _('Course Category')
        verbose_name_plural = _('Course Categories')

    def __str__(self):
        return self.title


class SkillRelatedExistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('skills') \
            .filter(skills__isnull=False)


class SkillCategory(models.Model):
    title = models.CharField(_('Title'), max_length=20)
    body = RichTextField(_('Text'), blank=True, null=True)

    created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

    objects = MultilingualManager()
    skill_exist = SkillRelatedExistManager()

    i18n = TranslationField(fields=('title', 'body'))

    class Meta:
        indexes = [GinIndex(fields=["i18n"])]
        verbose_name = _('Skill Category')
        verbose_name_plural = _('Skill Categories')

    def __str__(self):
        return self.title


class Course(models.Model):
    START_DATE_CHOICE = []
    for i in range(21):
        if i == 0:
            START_DATE_CHOICE.append((i, 'soon'))
        else:
            for ii in range(2010, 2031):
                START_DATE_CHOICE.append((ii, ii))
            break

    END_DATE_CHOICE = []
    for i in range(21):
        if i == 0:
            END_DATE_CHOICE.append((i, 'running'))
        else:
            for ii in range(2010, 2031):
                END_DATE_CHOICE.append((ii, ii))
            break

    user = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='courses', verbose_name=_('User'))
    category = models.ForeignKey(CourseCategory, related_name='courses', verbose_name=_('Category'),
                                 on_delete=models.CASCADE)

    title = models.CharField(_('Title'), max_length=20)
    source = models.CharField(_('Source'), blank=True, null=True, max_length=30)
    body = RichTextField(_('Text'), blank=True, null=True)
    start_on = models.IntegerField(_('Start On'), choices=START_DATE_CHOICE)
    end_on = models.IntegerField(_('End On'), choices=END_DATE_CHOICE, blank=True, null=True)

    created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

    i18n = TranslationField(fields=('title', 'source', 'body'))

    class Meta:
        indexes = [GinIndex(fields=["i18n"])]

    def __str__(self):
        return self.title


class Skill(models.Model):
    PERCENT_CHOICE = ()
    for i in range(101):
        PERCENT_CHOICE += ((i, i),)

    user = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='skills', verbose_name=_('User'))
    category = models.ForeignKey(SkillCategory, related_name='skills', verbose_name=_('Category'),
                                 on_delete=models.CASCADE)

    title = models.CharField(_('Title'), max_length=20)
    percent = models.IntegerField(choices=PERCENT_CHOICE)
    body = RichTextField(_('Text'), blank=True, null=True)

    created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

    i18n = TranslationField(fields=('title', 'body'))

    class Meta:
        indexes = [GinIndex(fields=["i18n"])]

    def __str__(self):
        return self.title
