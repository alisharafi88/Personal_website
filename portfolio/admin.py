from django.contrib import admin

from .models import Portfolio, ImgForPortfolio, LinkForPortfolio


class ImgInline(admin.StackedInline):
    model = ImgForPortfolio
    extra = 1


class LinkInline(admin.StackedInline):
    model = LinkForPortfolio
    extra = 1


class LinkAdmin(admin.ModelAdmin):
    model = LinkForPortfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['category', 'date']
    fieldsets = (
        ('detail', {'fields': ('category', 'client', 'date')}),
        ('description', {'fields': ('description', 'cover')})
    )
    inlines = (ImgInline, LinkInline)
