from django.urls import path

from creating_books import views

urlpatterns = [
    path('', views.create, name='create'),
]
