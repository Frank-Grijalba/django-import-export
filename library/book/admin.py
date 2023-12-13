from django.contrib import admin
from import_export import resources
from book.models import Book, Author, Category


class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "author",
        )


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
