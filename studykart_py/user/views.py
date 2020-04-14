from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.forms import LoginForm
from django.contrib.auth.models import User
from user.forms import StudentSignUpForm
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate,password_validation
from .models import user_profile
from user.models import roles
import pandas as pd
# Create your views here.


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            identifier = login_form.cleaned_data['identifier']
            password = login_form.cleaned_data['password']
            user=authenticate(request,username=identifier,password=password)
            if user != None:
                login_user(request,user)
                return redirect('main-page')
            else:
                return redirect('login')

    else:
        login_form = LoginForm()
    return render(request,'user/login.html',{'form':login_form})


def SignUpBuyer(request):
    if request.method == 'POST':
        signup_form = StudentSignUpForm(request.POST)
        if signup_form.is_valid():
            first_name = signup_form.cleaned_data['student_first_name']
            last_name = signup_form.cleaned_data['student_last_name']
            username = signup_form.cleaned_data['student_username']
            email = signup_form.cleaned_data['student_email']
            password = signup_form.cleaned_data['student_password']
            mobile = signup_form.cleaned_data['student_mobile']
            student = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            student_profile = user_profile.objects.create(user=student, user_mobile=mobile)
            buyer_role = roles.objects.get(pk=1)
            student.roles_set.add(buyer_role)
            return redirect('login')
        else:
            return render(request, 'user/signup_buyer.html', {'student_form': signup_form})
    else:
        signup_form = StudentSignUpForm()
        return render(request,'user/signup_buyer.html',{'student_form':signup_form})


def SignUpSeller(request):
    if request.method == 'POST':
        signup_form = StudentSignUpForm(request.POST)
        if signup_form.is_valid():
            first_name = signup_form.cleaned_data['student_first_name']
            last_name = signup_form.cleaned_data['student_last_name']
            username = signup_form.cleaned_data['student_username']
            email = signup_form.cleaned_data['student_email']
            password = signup_form.cleaned_data['student_password']
            mobile = signup_form.cleaned_data['student_mobile']
            student = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            student_profile = user_profile.objects.create(user=student,user_mobile=mobile)
            seller_role = roles.objects.get(pk=2)
            buyer_role = roles.objects.get(pk=1)
            student.roles_set.add(seller_role)
            student.roles_set.add(buyer_role)
            return redirect('login')
        else:
            return render(request, 'user/signup_seller.html', {'student_form': signup_form})
    else:
        signup_form = StudentSignUpForm()
        return render(request,'user/signup_seller.html',{'student_form':signup_form})


def filter(request):
    qs = user_profile.objects.all().values()    
    data = pd.DataFrame(qs)
    print(data)

    context = {
        'df' : data.to_html(),
        'describe' : data.describe().to_html()
    }

    return render(request, 'user/filtertemp.html', context)