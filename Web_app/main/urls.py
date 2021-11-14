from django.urls import path
from . import views


urlpatterns = [
    # главное меню
    path('', views.main, name='main'),
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('form3/', views.form3, name='form3'),
    path('form4/', views.form4, name='form4'),
    path('personalAccount/', views.personalAccount, name='personalAccount'),
    # path('message/', views.message, name='message'),



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
