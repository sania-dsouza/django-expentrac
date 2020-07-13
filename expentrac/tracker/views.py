from django import shortcuts
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Expense
from .forms import LoginForm, SignUpForm, TrackerRowForm
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


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
                return HttpResponseRedirect(reverse('tracker', args=(request.user.username,)))  # pointing to the generic tracker page currently
            else:
                messages.error(request, "Username and password didn't match.")
                return HttpResponseRedirect('/')

    else:
        form = LoginForm()

    return render(request, 'tracker/login.html', {'form': form})


def signup_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                fname = request.POST['first_name']
                lname = request.POST['last_name']
                user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
                return HttpResponseRedirect('/')
        except IntegrityError as e:
            messages.error(request, "Username already exists.")
            return render(request, 'tracker/signup.html', {'form': form})

    else:
        form = SignUpForm()

    return render(request, 'tracker/signup.html', {'form': form})


@login_required()
def tracker_page(request, username):
    categories = [verb_cat for code, verb_cat in Expense.CATEGORY_CHOICES]
    data = Expense.objects.filter(user=User.objects.get(username=username))
    if request.user.username == username:   # if the user changes the URL unwittingly or otherwise to that of another user, the page would require a login
        return shortcuts.render(request, 'tracker/trackerTable.html', {'categories': categories, 'object_list': data})
    else:
        return HttpResponseRedirect('/')


@login_required()
class TrackerRowCreate(BSModalCreateView):
    template_name = 'tracker/tracker_row_create.html'
    form_class = TrackerRowForm
    success_message = 'Success: Expense created.'


@login_required()
def create_expense_entry(request):
    if request.method == "POST":
        form = TrackerRowForm(request.POST)
        if form.is_valid():
            user = request.user   # get the user authenticated currently and mark expense against that user
            date = request.POST['date']
            item = request.POST['item']
            category = request.POST['category']
            amount = request.POST['amount']
            notes = request.POST['notes']
            Expense.objects.get_or_create(user=user, date=date, item=item, category=category, amount=amount, notes=notes)
            print("Submitting form for exp entry")
            return HttpResponseRedirect(reverse('tracker', args=(user.username,)))
    else:
        form = TrackerRowForm()

    return render(request, 'tracker/tracker_row_create.html', {'form': form})


class TrackerRowEdit(BSModalCreateView):
    template_name = 'tracker/tracker_row_edit.html'
    form_class = TrackerRowForm
    success_message = 'Success: Expense modified.'


@login_required()
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect('/')  # return to login page upon logout







