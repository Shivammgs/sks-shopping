from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from myapp.forms import Customuserform
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from ecomproject.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.conf import settings

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart



def register(request):
    form=Customuserform()
    if request.method=='POST':
        form=Customuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to continue")
            return redirect('/login')
    return render(request, 'myapp/authentication/register.html', {'form':form})




def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you have already logged in')
        return redirect('/')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
        return render(request, 'myapp/authentication/login.html')
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out successfully')
    return redirect('login')


def changepassword(request):
    if not request.user.is_authenticated:
        # Redirect to login if the user is not authenticated
        messages.error(request, 'You need to login to change your password.')
        return redirect('login')  # Use named URL patterns for better maintainability

    if request.method == 'POST':
        fm = SetPasswordForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)  # Prevents logging the user out
            messages.success(request, 'Password changed successfully!')
            return redirect('/')  # Redirect to profile or a similar page
        else:
            # # Error handling in case the form is invalid
            messages.error(request, 'Please fill the vacant data.')
    else:
        fm = SetPasswordForm(user=request.user)

    return render(request, 'myapp/authentication/changepassword.html', {'form': fm})



