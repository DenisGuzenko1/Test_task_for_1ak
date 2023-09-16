from django.contrib import admin

from .models import Users, Books, Register_books

admin.site.register(Users)
admin.site.register(Books)
admin.site.register(Register_books)