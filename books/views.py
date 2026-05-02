from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import  render
from django.urls import reverse_lazy
from django.db.models import Q
from accaunts.models import CustomUser
from books.forms import BookForm
from books.models import Author,Book,Barrow


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class MainView(ListView):
    model = CustomUser
    template_name = 'base.html'
    context_object_name = 'users'


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_navbar'] = True
        return context


class AuthorCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Author
    form_class = BookForm
    template_name = 'books/createauthor.html'
    success_url = reverse_lazy('create-book')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_navbar'] = True
        return context

class BookCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create_book.html'
    success_url = reverse_lazy('book-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_navbar'] = True
        return context


class BookUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create_book.html'
    success_url = reverse_lazy('book-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_navbar'] = True
        return context

class BookDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('kitoblar')


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_navbar'] = True
        return context


class MyBorrowsView(LoginRequiredMixin, ListView):
    model = Barrow
    template_name = 'books/my_borrows.html'
    context_object_name = 'borrows'

    def get_queryset(self):
        return Barrow.objects.filter(user=self.request.user)



class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        results = []

        if query:
            results = Book.objects.filter(
                Q(title__icontains=query) |
                Q(author__name__icontains=query) |
                Q(category__name__icontains=query)
            )

        return render(request, 'books/search.html', {
            'query': query,
            'books': results,
            'hide_navbar': True,
        })


