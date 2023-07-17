from django.urls import path
from user_account import views



urlpatterns = [
    #path('', views.login, name='index'),
    path('index/', views.index, name="index"),
    path('account/', views.account, name="account"),
    path('settings/', views.settings, name="settings"),
    path('subscriptions/', views.subscriptions, name="subscriptions"),
    # path('channels/', views.channels, name="channels"),
    # path('channels/', views.channels, name="channels"),
    # path('channels/', views.channels, name="channels"),
    # path('channels/', views.channels, name="channels"),
    # path('channels/', views.channels, name="channels"),
    # path('channels/', views.channels, name="channels"),
    # path('channels/', views.channels, name="channels"),
    # path('channels/', views.channels, name="channels")
    ]