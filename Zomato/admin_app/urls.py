from django.urls import path
from admin_app import views

urlpatterns = [
    path('login/', views.adminLogin, name='admin_login'),
    #path('loginchek/', views.logincheck, name = 'login_check')
]
