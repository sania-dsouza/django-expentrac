from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tracker
from .forms import LoginForm, SignUpForm, TrackerRowForm
from bootstrap_modal_forms.generic import BSModalCreateView


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
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = SignUpForm()

    return render(request, 'tracker/signup.html', {'form': form})


def tracker_page(request):
    categories = [verb_cat for code, verb_cat in Tracker.CATEGORY_CHOICES];
    return render(request, 'tracker/trackerTable.html', {'categories': categories})


class TrackerRowCreate(BSModalCreateView):
    template_name = 'tracker/tracker_row.html'
    form_class = TrackerRowForm
    success_message = 'Success: Expense created.'







