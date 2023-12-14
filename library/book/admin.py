from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from book.models import Book, Author, Category
from import_export.admin import ImportExportModelAdmin


admin.site.register(Book, ImportExportModelAdmin)
admin.site.register(Author, ImportExportModelAdmin)
admin.site.register(Category, ImportExportModelAdmin)


class BookResource(resources.ModelResource):
    full_title = Field()

    class Meta:
        model = Book

    # def dehydrate_full_title(self, book):
    #     return "%s by %s" % (book.name, book.author.name)


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
