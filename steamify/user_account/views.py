from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


def account(request):
    return render(request, 'account.html')

#@login_required(login_url='/usermanagement/index')
def settings(request):
    return render(request, 'settings.html')


def videoPage(request):
    return render(request, 'videoPage.html')

def subscriptions(request):
    return render(request, 'subscriptions.html')