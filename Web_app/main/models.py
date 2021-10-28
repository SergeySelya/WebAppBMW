from django.db import models

# Описание таблицы внутри БД


class Articles(models.Model):
    name = models.CharField('Имя', max_length=10, default="")
    tel = models.IntegerField('Телефон', max_length=13)

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
#     переименовывваем название таблицы в панеои администратора
#     class Meta:
#         verbose_name = "Заявка"
#         verbose_name_plural = "Заявки"
