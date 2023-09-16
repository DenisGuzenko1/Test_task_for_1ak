from django.urls import path

from index import views

urlpatterns = [
    path('<int:pk>/', views.user_page, name='user_page'),
    path('', views.index, name='index'),
    path('books<int:user_pk>/', views.books, name='books'),
    path('user_accounting<int:user_pk>/', views.user_accounting, name='user_accounting'),
    path('books_issued<int:user_id>/', views.books_issued, name='books_issued'),
    path('user_books<int:user_pk>/', views.user_books, name='user_books'),
    path('take_book/', views.take_book, name='take_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('error/', views.error, name='error'),
]
