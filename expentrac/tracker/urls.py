from django.urls import path

from . import views
from .models import User

urlpatterns = [
    # path('', views.base_page, name='base'),
    path('', views.login_page, name='login'),
    path('signup', views.signup_page, name='signup'),
    path('tracker', views.tracker_page, name='tracker'),
]
