# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from login.forms import SignUpForm, LoginForm

def signup(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            page_data = {"signup_form": signup_form}
            return render(request, 'login/signup.html', page_data)
    else:
        signup_form = SignUpForm()
        page_data = {"signup_form": signup_form}
        return render(request, 'login/signup.html', page_data)

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
<<<<<<< HEAD
                page_data = {"login_form": LoginForm()}
                return render(request, 'login/user_login.html', page_data)
    else:
        page_data = {"login_form": LoginForm()}
        return render(request, 'login/user_login.html', page_data)
=======
                return render(request, 'login/user_login.html', {"login_form": LoginForm})
    else:
        return render(request, 'login/user_login.html', {"login_form": LoginForm})
>>>>>>> 0d8ef7b (Adds user game entries, display and delete)

def user_logout(request):
    logout(request)
    return redirect("/")

