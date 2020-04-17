from django.urls import path
from admin_app import views

urlpatterns = [
    path('', views.adminLogin, name='admin_login'),
    path('country/', views.countryData, name ='country_data')
    #path('loginchek/', views.logincheck, name = 'login_check')
]
