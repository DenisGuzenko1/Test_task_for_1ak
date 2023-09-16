from django.shortcuts import render, redirect  # Импортируем render и redirect

from index.models import Users  # Импортируем модель Users из приложения index
from .forms import CreateUser  # Импортируем форму CreateUser из текущего приложения


# Эта функция обрабатывает запрос на регистрацию пользователя
def registration(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)  # Создаем экземпляр формы на основе данных из запроса

        if form.is_valid():  # Проверяем, прошла ли форма валидацию (введены ли данные правильно)
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            # Пытаемся найти пользователя с такими именем и фамилией в базе данных
            user = Users.objects.filter(name=name, surname=surname)

            if user.exists():
                # Если пользователь с такими данными уже существует, добавляем ошибку в форму
                form.add_error(None, f'Пользователь {name} {surname} уже существует!')
            else:
                # Если пользователь не был найден, сохраняем данные пользователя
                form.save()
                return redirect('index')  # Перенаправляем на страницу 'index'
        else:
            return form
    else:
        form = CreateUser()
    # Отображаем страницу 'register.html' с переданным контекстом
    return render(request, 'register.html', {'form': form})
