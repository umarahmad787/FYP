from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index'),
    #path('main', views.main_page),
    path('check', views.check_view),
    path('index', views.auth_view),
    path('signup/', views.signup_page)
    ]