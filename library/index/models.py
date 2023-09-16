from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'Имя')
    surname = models.CharField(max_length=40, verbose_name=u'Фамилия')
    patronymic = models.CharField(max_length=40, verbose_name=u'Отчество')

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class Books(models.Model):
    book_img = models.ImageField(upload_to='img/', blank=True, null=True, default=None)
    book_name = models.CharField(max_length=255, null=True)
    book_author = models.CharField(max_length=255, null=True)
    publication_date = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_DEFAULT, default=Users.objects.get(name='admin').id, )

    def __str__(self):
        return self.book_name


class Register_books(models.Model):
    user_id = models.CharField(max_length=60, null=True, blank=True)
    user_name = models.CharField(max_length=60, null=True, blank=True)
    user_surname = models.CharField(max_length=60, null=True, blank=True)
    book_name = models.CharField(max_length=60, null=True, blank=True)
    book_id = models.CharField(max_length=60, null=True, blank=True)
    date_take = models.DateField(null=True, blank=True)
    date_return = models.DateField(null=True, blank=True)
