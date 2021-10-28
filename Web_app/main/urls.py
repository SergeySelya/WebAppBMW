from django.urls import path
from . import views


urlpatterns = [
    # главное меню
    path('', views.main, name='main'),
    path('form', views.form1, name='form'),
    path('personalAccount/', views.personalAccount, name='personalAccount'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),

    # страница авторизации и регистрации
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('exit/', views.exit, name='exit'),

    # личный кабинет
    path('personalAccount/<int:pk>/', views.checkInfo.as_view(), name='checkInfo'),
    path('personalAccount/<int:pk>/update/', views.updateInfo.as_view(), name='updateInfo'),
    path('personalAccount/<int:pk>/delete', views.deleteInfo.as_view(), name='deleteInfo'),

]
