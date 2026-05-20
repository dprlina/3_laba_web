from django.contrib import admin
from .models import Author, Genre, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year')
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'published_year', 'is_available')
    list_filter = ('is_available', 'genres', 'published_year')
    filter_horizontal = ('genres',)