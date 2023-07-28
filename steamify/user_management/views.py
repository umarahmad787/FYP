from django.shortcuts import render, HttpResponse, redirect
#import mysql.connector as sql
from django.contrib.auth import logout
from django.db import connection as conn
from django.contrib import messages


firstname=''
lastname=''
username=''
email=''
password=''
gender=''

# Create your views here.
def login_view(request):
    logout(request)
    return render(request, 'login.html')



def logout_view(request):
    logout(request)  # Ends the user's session
    return redirect('/usermanagement/login')



def signup_page(request):
    return render(request, 'register.html')



def auth_view(request):
    if request.method == "POST":
        # Perform login authentication
        cursor = conn.cursor()
        username = request.POST.get('username')
        password = request.POST.get('password')
        query = "SELECT * from user_management_logininfo WHERE username='{}' AND password='{}'".format(username, password)
        cursor.execute(query)
        authenticated=tuple(cursor.fetchall())
        if authenticated:  # Replace with your authentication logic
            # Save user session
            request.session['authenticated'] = True
            request.session['username'] = username
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
            global username,email,password   
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')       
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            if not username or not email or not password or not firstname or not lastname or not gender:
                msg = 'Please provide all the required information.'
                messages.error(request, msg)
                return render(request, 'register.html')
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM user_management_logininfo WHERE username=%s OR email=%s", [username, email])
            existing_user = cursor.fetchone()
            if existing_user:
                if existing_user[0] == username:
                    messages.error(request, 'Username is already taken.')
                if existing_user[1] == email:
                    messages.error(request, 'Email is already registered.')
                return render(request, 'register.html')
            c = "INSERT INTO user_management_logininfo (username, email, password, firstname, gender, lastname) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (username, email, password, firstname, gender, lastname)
            cursor.execute(c, values)
            conn.commit()
            return render(request, 'login.html')  # Redirect to index success page
        elif 'login_page' in request.POST:
            
            # Handle create account action
            return render(request, 'login.html')  # Redirect to login page
    else:
        return HttpResponse(' Authentications Failed ')

