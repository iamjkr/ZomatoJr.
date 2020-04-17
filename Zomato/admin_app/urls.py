from django.urls import path
from admin_app import views

urlpatterns = [
    path('', views.adminLogin, name='admin_login'),
    path('country/', views.countryData, name ='country'),
    path('state/', views.stateData, name ='state'),
    path('city/', views.cityData, name='city'),
    path('region/', views.regionData, name='region'),
    path('resto/', views.restoData, name='resto'),
    #path('loginchek/', views.logincheck, name = 'login_check')
]
