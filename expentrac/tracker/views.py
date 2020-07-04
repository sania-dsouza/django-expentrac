from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tracker
from .forms import LoginForm


def base_page(request):
    return render(request, 'tracker/base.html')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = LoginForm()

    return render(request, 'tracker/login.html', {'form': form})


def signup_page(request):
    return render(request, 'tracker/signup.html')


def tracker_page(request):
    categories = [verb_cat for code, verb_cat in Tracker.CATEGORY_CHOICES];
    return render(request, 'tracker/trackerTable.html', {'categories': categories})




