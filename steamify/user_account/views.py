from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection as conn

# Create your views here.

def index(request):
    if request.session.get('authenticated') == True:
        email = request.session.get('email')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM user_management_logininfo WHERE email=%s", [email])
        username = cursor.fetchone()[0]
        return render(request, 'index.html', {'username': username})
    else:
        return render(request, 'login.html')


def payment(request):

    
    if request.session.get('authenticated') == True:
        subscription = request.GET.get('subscription')
        email = request.session.get('email')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM user_management_logininfo WHERE email=%s", [email])
        username = cursor.fetchone()[0]
        
        return render(request, 'payment.html', {'subscription': subscription,'username': username})

#@login_required(login_url='/usermanagement/index')
def settings(request):
    # if not request.user.is_authenticated:
    #     return redirect('/usermanagement/index')
    if request.session.get('authenticated') == True:
        email = request.session.get('email')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM user_management_logininfo WHERE email=%s", [email])
        username = cursor.fetchone()[0]
        return render(request, 'settings.html', {'username': username})
    else:
        return render(request, 'login.html')


def videoPage(request):
    return render(request, 'videoPage.html')



def subscriptions(request):
    email = request.session.get('email')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM user_management_logininfo WHERE email=%s", [email])
    username = cursor.fetchone()[0]
    return render(request, 'subscriptions.html', {'username': username})