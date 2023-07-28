from django.urls import path
from user_account import views



urlpatterns = [
    #path('', views.login, name='index'),
    path('index/', views.index, name="index"),
    path('paymentPage/', views.paymentPage, name="paymentPage"),
    path('settings/', views.settings, name="settings"),
    path('changePassword/', views.changePassword, name="changePassword"),
    path('accountDetails/', views.myAccountDetails, name="accountDetails"),
    path('subscriptions/', views.subscriptions, name="subscriptions"),
    path('subscriptionDetails/', views.subscriptionDetails, name="subscriptionDetails"),
    path('paymentProcess/', views.paymentProcess, name="paymentProcess"),
    path('cancelSubscription/', views.cancelSubscription, name="cancelSubscription"),
    path('videoPage/', views.videoPage, name="videoPage")
    ]