from django.shortcuts import render, HttpResponse
#import mysql.connector as sql
from django.db import connection as conn

uname=''
email=''
password=''


# Create your views here.
def index(request):
    return render(request, 'signup.html')



def signup_view(request):
    return HttpResponse('signup here')


def auth_view(request):
    #if request.method == "POST":
    global email,password
    if request.method == "POST":
        #conn = sql.     (host="localhost",user="umar",passwd="878876",database="streamify_db")
        #conn = connection
        cursor = conn.cursor()
        d = request.POST
        print(d)
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="password":
                password=value
                # print(passwd)
                # print(email)
        c = "SELECT * from user_management_logininfo WHERE email='{}' AND password='{}'".format(email, password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return(HttpResponse('auth error'))
        else:
            return render(request,'main.html')
    # elif 'create_account' in request.POST:
    #     # Handle create account action
    #     return render(request, 'signup.html')  # Redirect to signup page 
    else:
        return render(request, 'signup.html')
        
    
    
    
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
            c = "INSERT INTO user_management_logininfo (username, email, password) Values('{}','{}','{}') ".format(uname, email, password)
            cursor.execute(c)
            conn.commit()
            # Handle login action
            # Perform authentication logic here
            return render(request, 'subs_plans.html')  # Redirect to login success page
        elif 'login_page' in request.POST:
            
            # Handle create account action
            return render(request, 'login.html')  # Redirect to signup page
    else:
        # Render the form initially
        #return redirect(request, 'signup')
        return HttpResponse(' Authentications Failed ')

