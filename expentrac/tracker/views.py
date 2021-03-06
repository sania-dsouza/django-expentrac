import time

from django import shortcuts
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.models import User
import calendar, datetime

from django.views import generic

from .models import Expense
from .forms import LoginForm, SignUpForm, TrackerRowForm
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def get_month(date):
    return calendar.month_name[date.month]


def get_year(date):
    return date.year


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
                time.sleep(2)
                login(request, user)
                return HttpResponseRedirect(reverse('tracker', args=(request.user.username,)))
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
    month_year = []
    categories = [verb_cat for code, verb_cat in Expense.CATEGORY_CHOICES]
    data = Expense.objects.filter(user=User.objects.get(username=username))
    for exp_item in data:  # get the month and year of each exp item and append to the list for the filters
        m = get_month(exp_item.date)
        y = get_year(exp_item.date)
        month_year.append(str(m)+" "+str(y))
    month_year = set(month_year)  # remove duplicates

    # code to calculate the total expense after each row of expense
    initial = 0
    for exp_item in data:
        total_after_exp = initial + exp_item.amount
        initial = initial + exp_item.amount
        exp_item.total_after_expense = total_after_exp   # adding another attribute to the object : total_after_expense

    if request.user.username == username:   # if the user changes the URL unwittingly or otherwise to that of another user, the page would require a login
        return shortcuts.render(request, 'tracker/trackerTable.html', {'categories': categories, 'month_year': month_year, 'object_list': data})
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
            # print("Submitting form for exp entry")
            return HttpResponseRedirect(reverse('tracker', args=(user.username,)))
    else:
        form = TrackerRowForm()

    return render(request, 'tracker/tracker_row_create.html', {'form': form})


class TrackerRowEdit(BSModalCreateView):
    template_name = 'tracker/tracker_row_edit.html'
    form_class = TrackerRowForm
    # success_message = 'Success: Expense modified.'


@login_required()
def edit_expense_entry(request, id):
    current_exp = Expense.objects.get(pk=id)
    variables = {'form': TrackerRowForm(instance=current_exp)}

    # return render(request, 'tracker/tracker_row_edit.html', variables)
    if request.method == "POST":
        form = TrackerRowForm(request.POST)
        if form.is_valid():
            user = request.user   # get the user authenticated currently and mark expense against that user
            date = request.POST['date']
            # print(date)
            item = request.POST['item']
            category = request.POST['category']
            amount = request.POST['amount']
            notes = request.POST['notes']
            e = Expense.objects.get(pk=id)
            e.user = user
            # print(current_exp.date == date)
            e.date = date
            e.item = item
            e.category = category
            e.amount = amount
            e.notes = notes
            e.save()
            # print("Submitting form for exp entry")
            return HttpResponseRedirect(reverse('tracker', args=(user.username,)))
        else:
            user = request.user
            return HttpResponseRedirect(reverse('tracker', args=(user.username,)))
    else:
        pass
        # form = TrackerRowForm(instance=current_exp)

    return render(request, 'tracker/tracker_row_edit.html', variables)


@login_required()
def delete_expense_entry(request, id):
    current_exp = Expense.objects.get(pk=id)
    user = request.user
    e = Expense.objects.get(pk=id)
    time.sleep(2)
    e.delete()
    return HttpResponseRedirect(reverse('tracker', args=(user.username,)))


@login_required()
def logout_view(request):
    time.sleep(2)
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect('/')  # return to login page upon logout


def page_not_found(request, exception):    # 404 page view
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return shortcuts.render(request, 'tracker/404.html')


def no_resource(request):     # 500 page view
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return shortcuts.render(request, 'tracker/500.html')






