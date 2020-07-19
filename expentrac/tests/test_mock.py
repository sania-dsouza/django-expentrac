# mock test file
import pytest
from django.contrib.auth import login
from django.db import IntegrityError
from django.test import Client, SimpleTestCase
from django.urls import reverse

from datetime import date
from django.contrib.auth.models import User


# def f(i):
#     return i+1
#
#
# def test_f():
#     assert f(2) == 3


# create test data to run tests on: This will either create a new user or use an existing one if present
@pytest.fixture()
def create_user():
    try:
        u = User.objects.create_user(username = "pytestuser", email = "pytest@pytest.com", password = "pytestpass")
    except IntegrityError:
        return User.objects.get(username="pytestuser")

    return u


# def create_expense(user):
#     return Expense.objects.get_or_create(user, date.today(), "Pytest data", "Fuel", 123.0, "pytest test data")

@pytest.mark.django_db
def test_login(create_user):
    # u = create_user()   # create a new user or get one if already present
    c = Client()
    c.login(username=create_user.username, password=create_user.password)
    response = c.get(reverse('tracker', kwargs={'username': create_user.username}), follow=True)
    assert response.status_code == 200







