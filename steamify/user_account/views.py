from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection as conn
from user_account.models import SubscribedUsers 
from user_management.models import loginInfo
from django.contrib import messages
from datetime import datetime, timedelta



# Create your views here.

def index(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        return render(request, 'index.html', {'username': username})
    else:
        return render(request, 'login.html')



def myAccountDetails(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        try:
            logininfo = loginInfo.objects.get(username=username)
            subscribed_user = SubscribedUsers.objects.get(username=username)
            subscription_status = "Active"
            context = {
            'userEmail': logininfo.email,
            'userFname': logininfo.firstname,
            'userLname': logininfo.lastname,
            'Uname': logininfo.username,
            'subscription_status': subscription_status,
        }
            return render(request, 'accountDetails.html',{'username' : username, 'context' : context})
        except SubscribedUsers.DoesNotExist:
            subscription_status = ""
            context = {
            'userEmail': logininfo.email,
            'userFname': logininfo.firstname,
            'userLname': logininfo.lastname,
            'Uname': logininfo.username,
            'subscription_status': subscription_status,
        }
            return render(request, 'accountDetails.html',{'username' : username, 'context' : context})
            #return HttpResponse('database issue')
        
    return redirect('index')



def settings(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        return render(request, 'settings.html', {'username': username})
    else:
        return redirect('index')



#@login_required(login_url='/usermanagement/index')
def changePassword(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        if request.method == 'POST':
            username = request.session.get('username')
            current_password = request.POST.get('currentPassword')
            new_password = request.POST.get('newPassword')

            try:
                logininfo = loginInfo.objects.get(username=username)
            except loginInfo.DoesNotExist:
                return redirect('index')  # Handle the error gracefully

            if logininfo.password == current_password:
                # If the current password matches, update the password
                logininfo.password = new_password
                logininfo.save()
                messages.success(request, 'Password updated successfully!')
            else:
                # If the current password does not match, show an error message
                messages.error(request, 'Your current password is incorrect.')

            return render(request, 'settings.html', {'username': username})
        #return render(request, 'settings.html', {'username': username})
        return HttpResponse('error')
    else:
        return redirect('index')






def subscriptions(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        return render(request, 'subscriptions.html', {'username': username})
    else:
        return redirect('index')






def subscriptionDetails(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        try:
            subscribed_user = SubscribedUsers.objects.get(username=username)
            subscription_status = "Active"

            # subscriptionDate to Expiry Date    
            subscriptiondate = subscribed_user.subscription_date
            subscriptionDateSTR = str(subscriptiondate)
            subscriptionDatestr = datetime.strptime(subscriptionDateSTR, "%Y-%m-%d")
            next_month = subscriptionDatestr.month % 12 + 1
            year_for_next_month = subscriptionDatestr.year + subscriptionDatestr.month // 12
            subscriptionExpirydate = subscriptionDatestr.replace(month=next_month, year=year_for_next_month)


            context = {
                'subsciptionDate': subscribed_user.subscription_date,
                'subscriptionExpirydate': subscriptionExpirydate,
                'subscription_status': subscription_status,
            }
            return render(request, 'subscriptionDetails.html', {'username': username, 'context': context})
        except SubscribedUsers.DoesNotExist:
            subscription_status = ""   
            return render(request, 'subscriptionDetails.html', {'username': username, 'subscription_status': subscription_status})

    return redirect('index')





def paymentProcess(request):
    #if request.user.is_authenticated:
    if request.session.get('authenticated') == True:  
        if request.method == 'POST':
            username = request.session.get('username')
            card_number = request.POST.get('cardNumber')
            cardholder_name = request.POST.get('cardName')
            expiry_date = request.POST.get('expiryDate')
            cvv = request.POST.get('cvv')

            # Get the username from the session if the user is logged in
            #username = None
            

            # Create a new SubscribedUsers instance and save it to the database
            subscribed_user = SubscribedUsers.objects.create(
                username=username,
                card_number=card_number,
                cardholder_name=cardholder_name,
                expiry_date=expiry_date,
                cvv=cvv
            )
            messages.success(request, 'Congratulations! You are now Subscribed.')
            return redirect('subscriptionDetails')
        else:
            return render(request, 'index.html', {'username': username})
    
    else:
        return redirect('index')
    






def paymentPage(request):
    if request.session.get('authenticated') == True:
        subscription = request.GET.get('subscription')
        username = request.session.get('username')

        # Check if the username exists in the SubscribedUsers table
        try:
            subscribed_user = SubscribedUsers.objects.get(username=username)
            messages.success(request, 'Your are already subscribed.')
            return redirect('/useraccount/subscriptionDetails/')
        except SubscribedUsers.DoesNotExist:
            # If the username is not found, render the payment page
            return render(request, 'payment.html', {'subscription': subscription, 'username': username})
    else:
        # Handle the case when the user is not authenticated or 'authenticated' key is not present in the session
        return redirect('index')  # Redirect to the login page or handle it as per your application's logic





def cancelSubscription(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        try:
            subscribed_user = SubscribedUsers.objects.get(username=username)
            subscribed_user.delete()
            messages.success(request, 'Your subscription is now canceled.')  # Success message
            return redirect('subscriptionDetails')
        except SubscribedUsers.DoesNotExist:
            messages.success(request, 'Your are not subscribed.')
            #HttpResponse('your are already not subscribed')
            return redirect('subscriptionDetails')
    else:
        return redirect('index')




def videoPage(request):
    if request.session.get('authenticated') == True:
        username = request.session.get('username')
        try:
            subscribed_user = SubscribedUsers.objects.get(username=username)
            return render(request, 'videoPage.html',{'username' : username})

        except SubscribedUsers.DoesNotExist:
            messages.error(request, 'Your are currently not Subscribed.')
            return render(request, 'notSubscribed.html',{'username' : username})
    else:
        return redirect('index')