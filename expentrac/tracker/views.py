from django.shortcuts import render
from .models import Tracker

def base_page(request):
    return render(request, 'tracker/base.html')


def login_page(request):
    return render(request, 'tracker/login.html')


def signup_page(request):
    return render(request, 'tracker/signup.html')


def tracker_page(request):
    categories = [verb_cat for code, verb_cat in Tracker.CATEGORY_CHOICES];
    return render(request, 'tracker/trackerTable.html', {'categories': categories})
