from django.contrib import admin
from .models import Articles, ServiceForm

# Регистрация таблицы в панели администратора
admin.site.register(Articles)
admin.site.register(ServiceForm)
