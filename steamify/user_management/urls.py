from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('check', views.check_view),
    path('index', views.auth_view),
    path('signup/', views.signup_page)
    ]