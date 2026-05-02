from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            login(request, user)
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "account/register.html", {"form": form,'hide_navbar': True })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main-page")
        else:
            return render(request, "account/login.html", {"error": "Username yoki password xato"})

    return render(request, "account/login.html",{'hide_navbar': True })


def user_logout(request):
    logout(request)
    return redirect("login")