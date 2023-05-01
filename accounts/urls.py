from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('', views.home,name='home'),
    path('registerpage/', views.registerPage, name="registerpage"),
    path('loginpage/', views.loginPage, name="loginpage"),
    path('logout/', views.logoutUser, name="logout"),
]