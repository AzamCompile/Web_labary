from django.urls import path
from .views import (
    MainView,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    AuthorCreateView,
    MyBorrowsView,
    SearchView,
)

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='create_book'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='update_book'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='delete-book'),
    path('authors/create/', AuthorCreateView.as_view(), name='create-author'),
    path('my-borrows/', MyBorrowsView.as_view(), name='my-borrows'),
    path('search/', SearchView.as_view(), name='search'),
]