from django.urls import path
from restaurant import views

urlpatterns = [
    path('', views.indexview, name='index_page'),
    #path('loginchek/', views.logincheck, name = 'login_check')
]
