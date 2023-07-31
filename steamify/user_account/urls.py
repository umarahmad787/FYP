from django.urls import path
from user_account import views
from django.conf.urls.static import static
from django.conf import settings



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
    path('videoPage/<int:video_id>/', views.videoPage, name="videoPage"),
    path('upload_video/', views.upload_video, name="upload_video"),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)