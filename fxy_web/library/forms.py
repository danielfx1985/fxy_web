from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'file']
        labels = {
            'title': '书名','author': '作者','description': '简介','file': '文件内容',
        }