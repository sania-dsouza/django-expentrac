from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tracker
from .forms import LoginForm, SignUpForm, TrackerRowForm
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def base_page(request):
    return render(request, 'tracker/base.html')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/tracker')  # pointing to the generic tracker page currently
            else:
                return HttpResponseRedirect('/')

    else:
        form = LoginForm()

    return render(request, 'tracker/login.html', {'form': form})


def signup_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            user = User.objects.create_user(username=username, email=email, password = password, first_name = fname, last_name=lname)
            return HttpResponseRedirect('/')

    else:
        form = SignUpForm()

    return render(request, 'tracker/signup.html', {'form': form})


def tracker_page(request):
    categories = [verb_cat for code, verb_cat in Tracker.CATEGORY_CHOICES];
    return render(request, 'tracker/trackerTable.html', {'categories': categories})


class TrackerRowCreate(BSModalCreateView):
    template_name = 'tracker/tracker_row_create.html'
    form_class = TrackerRowForm
    success_message = 'Success: Expense created.'


class TrackerRowEdit(BSModalCreateView):
    template_name = 'tracker/tracker_row_edit.html'
    form_class = TrackerRowForm
    success_message = 'Success: Expense modified.'







