from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from book.models import Book, Author, Category


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)


# class BookResource(resources.ModelResource):
#     class Meta:
#         model = Book
#         fields = (
#             "id",
#             "name",
#             "author__name",
#         )


# It is possible to override a resource field to change some of its options:
class BookResource(resources.ModelResource):
    published = Field(attribute="published", column_name="published_date")
    # Other fields that don’t exist in the target model may be added
    myField = Field(column_name='myownfield')

    class Meta:
        model = Book


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
