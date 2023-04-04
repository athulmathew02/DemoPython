from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

from banksapp.forms import RegistrationForm, RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4, \
    RegistrationForm5
from .models import district,branch




# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('forms')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')




def FormPage(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Application accepted')
            return render(request, 'forms.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

        form1 = RegistrationForm1(request.POST)
        if form1.is_valid():
            messages.success(request, 'Application accepted')
            return render(request, 'forms.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form1.errors)

        form2 = RegistrationForm2(request.POST)
        if form2.is_valid():
            messages.success(request, 'Application accepted')
            return render(request, 'forms.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form2.errors)

        form3 = RegistrationForm3(request.POST)
        if form3.is_valid():
            messages.success(request, 'Application accepted')
            return render(request, 'forms.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form3.errors)

        form4 = RegistrationForm4(request.POST)
        if form4.is_valid():
            messages.success(request, 'Application accepted')
            return render(request, 'forms.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form4.errors)

        form5 = RegistrationForm5(request.POST)
        if form5.is_valid():
            messages.success(request, 'Application accepted')
            return render(request, 'forms.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form5.errors)
    else:
            form = RegistrationForm()
    return render(request, 'forms.html')


def getdata(request):
    distcontext = district.objects.all()
    branchcontext = branch.objects.all()
    return render(request,'forms.html', {'district':distcontext, 'branch': branchcontext})

















































