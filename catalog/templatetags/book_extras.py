from django import template
from django.utils.html import mark_safe
from datetime import datetime

register = template.Library()

# КАСТОМНЫЙ ФИЛЬТР №1
@register.filter
def currency(value, symbol='₽'):
    try:
        formatted = f"{value:,.2f}".replace(",", " ")
        return f"{formatted} {symbol}"
    except:
        return value

# КАСТОМНЫЙ ФИЛЬТР №2 (для звездочек - если спросят)
@register.filter
def stars_rating(value):
    try:
        rating = min(5, max(1, round(int(value) / 100)))
        return mark_safe('★' * rating + '☆' * (5 - rating))
    except:
        return '☆☆☆☆☆'

# КАСТОМНЫЙ ТЕГ №1
@register.simple_tag
def current_year():
    return datetime.now().year

# КАСТОМНЫЙ ТЕГ №2
@register.simple_tag
def book_status(book):
    if book.is_available:
        return mark_safe('<span class="badge bg-success">В наличии</span>')
    return mark_safe('<span class="badge bg-danger">Нет в наличии</span>')

# КАСТОМНЫЙ ТЕГ №3 (inclusion tag)
@register.inclusion_tag('includes/book_card.html')
def book_card(book, show_rating=True):
    return {'book': book, 'show_rating': show_rating}