from django.shortcuts import render


def base_page(request):
    return render(request, 'tracker/base.html')


def login_page(request):
    return render(request, 'tracker/login.html')


def signup_page(request):
    return render(request, 'tracker/signup.html')
