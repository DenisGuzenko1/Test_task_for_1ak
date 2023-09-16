from datetime import datetime

from django.shortcuts import render, redirect

from .models import Users, Register_books, Books


def user_page(request, pk):
    # Получаем пользователя по его ID
    user = Users.objects.get(id=pk)

    # Получаем все записи регистрации книг
    registration = Register_books.objects.all()

    # Создаем контекст для передачи данных в шаблон
    context = {
        'registration': registration,
        'user': user,
    }

    # Отображаем страницу пользователя
    return render(request, 'user_page.html', context)


def index(request):
    # Получаем всех пользователей, сортируем по фамилии
    users = Users.objects.all().order_by('surname')

    # Создаем контекст для передачи данных в шаблон
    context = {
        "users": users
    }

    # Отображаем главную страницу
    return render(request, 'index.html', context)


def user_accounting(request, user_pk):
    # Получаем пользователя по его ID
    user = Users.objects.get(id=user_pk)

    # Получаем все записи регистрации книг
    registration = Register_books.objects.all()

    # Создаем контекст для передачи данных в шаблон
    context = {
        'registration': registration,
        'user': user,
    }

    # Отображаем страницу учета пользователя
    return render(request, 'user_accounting.html', context)


def books(request, user_pk):
    # Получаем ID администратора
    admin = Users.objects.get(name='admin').id

    # Получаем все книги, принадлежащие администратору, и сортируем по автору
    books = Books.objects.all().filter(user=admin).order_by('book_author')

    # Получаем пользователя по его ID
    user = Users.objects.get(id=user_pk)

    # Создаем контекст для передачи данных в шаблон
    context = {
        'books': books,
        'user_pk': user_pk,
        'user': user
    }

    # Отображаем страницу списка книг
    return render(request, 'books_list.html', context)


def user_books(request, user_pk):
    # Получаем все книги, принадлежащие пользователю, и сортируем по автору
    books = Books.objects.all().filter(user=user_pk).order_by('book_author')

    # Создаем контекст для передачи данных в шаблон
    context = {
        'books': books,
        'user_pk': user_pk
    }

    # Отображаем страницу книг пользователя
    return render(request, 'user_books.html', context)


def books_issued(request, user_id):
    # Получаем пользователя по его ID
    admin = Users.objects.get(name='admin')

    # Получаем все книги, не принадлежащие администратору
    users_books = Books.objects.all().exclude(user=admin)

    # Создаем контекст для передачи данных в шаблон
    context = {
        'user_id': user_id,
        'users_books': users_books,
    }

    # Отображаем страницу выданных книг
    return render(request, 'books_issued.html', context)


def take_book(request):
    if request.method == 'POST':
        # Получаем ID книги и пользователя из POST-запроса
        book_id = request.POST['book_number']
        user_id = request.POST['user_id']

        # Получаем ID администратора
        admin = Users.objects.get(name='admin').id

        # Получаем пользователя по его ID
        user = Users.objects.get(id=user_id)

        # Получаем текущую дату и время
        take_date = datetime.now()

        try:
            # Находим книгу, принадлежащую администратору, по ее ID
            book = Books.objects.filter(user=admin).get(id=book_id)

            # Присваиваем книге нового пользователя и сохраняем изменения
            book.user = user
            book.save()

            # Создаем запись о выдаче книги и сохраняем ее
            register = Register_books(user_name=user.name, user_surname=user.surname, book_name=book.book_name,
                                      user_id=user_id, book_id=book_id, date_take=take_date)
            register.save()

            # Перенаправляем на главную страницу
            return redirect('index')
        except:
            # В случае ошибки перенаправляем на страницу ошибки
            return redirect('error')


def return_book(request):
    if request.method == 'POST':
        # Получаем ID книги и пользователя из POST-запроса
        book_id = request.POST['book_number']
        user_id = request.POST['user_id']

        # Получаем администратора
        admin = Users.objects.get(name='admin')

        # Получаем текущую дату и время
        return_date = datetime.now()
        try:
            # Находим книгу, принадлежащую пользователю, по ее ID
            book = Books.objects.filter(user=user_id).get(id=book_id)

            # Возвращаем книгу администратору и сохраняем изменения
            book.user = admin
            book.save()

            # Находим последнюю запись о выдаче этой книги пользователю
            register = Register_books.objects.filter(user_id=user_id, book_id=book_id).last()

            # Устанавливаем дату возврата и сохраняем изменения
            register.date_return = return_date
            register.save()

            # Перенаправляем на главную страницу
            return redirect('index')
        except:
            # В случае ошибки перенаправляем на страницу ошибки
            return redirect('error')


def error(request):
    # Отображаем страницу ошибки
    return render(request, 'error_page.html')
