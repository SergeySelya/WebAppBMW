from django.db import models

# Описание таблицы внутри БД


class Articles(models.Model):
    name = models.CharField('Имя', max_length=10, default="")
    tel = models.IntegerField('Телефон')

    def __str__(self):
        return self.name


class ServiceForm(models.Model):

    login = models.CharField('Логин', max_length=20, default='gg')
    name = models.CharField('Имя', max_length=10, default='')
    tel = models.IntegerField('Телефон')
    type_work = models.TextField('Комментарий')
    date = models.DateField('Дата записи')
    time = models.TimeField('Время записи')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/personalAccount/{self.id}/'

