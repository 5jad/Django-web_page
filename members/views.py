from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, SignUpForm
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Hello Guys')  
            else:
                return HttpResponse("Invalid login details provided.")
        else:
            return HttpResponse("Form is not valid.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login') 
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})