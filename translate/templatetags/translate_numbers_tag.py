from django import template
from django.utils import translation


register = template.Library()


@register.filter
def translate(number):
    input_number = str(number)
    english = '0123456789'
    persian = '۰۱۲۳۴۵۶۷۸۹'
    translation_table = ''
    current_language = translation.get_language()

    if current_language == 'fa':
        translation_table = input_number.maketrans(english, persian)
    elif current_language == 'en':
        translation_table = input_number.maketrans(persian, english)
    else:
        return number
    return input_number.translate(translation_table)
