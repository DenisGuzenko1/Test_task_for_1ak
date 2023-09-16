from django import forms

from index.models import Books


class New_book(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_img', 'book_name', 'book_author']
