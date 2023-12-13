from django.contrib import admin
from import_export import resources
from book.models import Book, Author, Category


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)


class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "author__name",
        )


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
