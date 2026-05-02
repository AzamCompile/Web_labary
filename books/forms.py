from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'published_date', 'count']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'author': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'category': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border rounded-lg'}),
            'count': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }