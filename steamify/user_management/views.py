from django.shortcuts import render, HttpResponse, redirect
#import mysql.connector as sql
from django.contrib.auth import logout
from django.db import connection as conn
from django.contrib import messages
uname=''
email=''
password=''

# Create your views here.
def login_view(request):
    logout(request)
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Ends the user's session
    return redirect('/usermanagement/login')

def signup_page(request):
    return render(request, 'register.html')


# def auth_view(request):
#     #if request.method == "POST":
#     global email,password
#     if request.method == "POST":
#         cursor = conn.cursor()
#         d = request.POST
#         print(d)
#         for key,value in d.items():
#             if key=="email":
#                 email=value
#             if key=="password":
#                 password=value
#         c = "SELECT * from user_management_logininfo WHERE email='{}' AND password='{}'".format(email, password)
#         cursor.execute(c)
#         t=tuple(cursor.fetchone())
#         if t==():
#             return(HttpResponse('auth error'))
#         else:
#             return render(request,'index.html')
#     elif 'index-page' in request:
#         # Handle create account action
#         return render(request, 'index.html')  # Redirect to signup page 
#     else:
#         return render(request, 'login.html')


def auth_view(request):
    if request.method == "POST":
        # Perform login authentication
        cursor = conn.cursor()
        email = request.POST.get('email')
        password = request.POST.get('password')
        c = "SELECT * from user_management_logininfo WHERE email='{}' AND password='{}'".format(email, password)
        cursor.execute(c)
        authenticated=tuple(cursor.fetchall())
        if authenticated:  # Replace with your authentication logic
            # Save user session
            request.session['authenticated'] = True
            request.session['email'] = email

            #username from sql and render with page
            cursor.execute("SELECT username FROM user_management_logininfo WHERE email=%s", [email])
            username = cursor.fetchone()[0]

            return render(request, 'index.html', {'username': username})
        else:
            logout(request)
            messages.error(request, 'Invalid Email or Password')
            return render(request, 'login.html')
    else:
        # Handle GET request for login page
        logout(request)
        return render(request, 'login.html')
    
    
    
def check_view(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            global uname,email,password
            cursor = conn.cursor()
            d = request.POST
            for key,value in d.items():
                if key=="uname":
                    uname=value
                if key=="email":
                    email=value
                if key=="password":
                    password=value
            if not uname or not email or not password:
                msg = 'Please provide all the required information.'
                messages.error(request, msg)
                return render(request, 'register.html')
            cursor.execute("SELECT * FROM user_management_logininfo WHERE email=%s", [email])
            existing_user = cursor.fetchone()
            if existing_user:
                messages.error(request, 'Email is already registered.')
                return render(request, 'register.html')
            c = "INSERT INTO user_management_logininfo (username, email, password) Values('{}','{}','{}') ".format(uname, email, password)
            cursor.execute(c)
            conn.commit()
            return render(request, 'login.html')  # Redirect to index success page
        elif 'login_page' in request.POST:
            
            # Handle create account action
            return render(request, 'login.html')  # Redirect to login page
    else:
        return HttpResponse(' Authentications Failed ')

