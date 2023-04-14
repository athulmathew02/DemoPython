from django.urls import path
from banksapp import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('register/', views.SignupPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('forms/', views.FormPage, name='forms'),

]
