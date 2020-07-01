from django.urls import path

from . import views

urlpatterns = [
    #path('', views.base_page, name='base'),
    path('', views.login_page, name='login'),
]
