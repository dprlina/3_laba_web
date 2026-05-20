from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.select_related('author').prefetch_related('genres').all()
    return render(request, 'book_list.html', {'books': books})