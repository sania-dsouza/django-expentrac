from django.urls import path

from . import views
# from .models import User

urlpatterns = [
    # path('', views.base_page, name='base'),
    path('', views.login_page, name='login'),
    path('signup', views.signup_page, name='signup'),
    path('tracker/<username>', views.tracker_page, name='tracker'),
    # path('tracker', views.tracker_page, name='tracker'),
    path('create/', views.create_expense_entry, name='tracker_row_create'),
    path('edit/<int:id>', views.edit_expense_entry, name='tracker_row_edit'),
    path('delete/<int:id>', views.delete_expense_entry, name='tracker_row_delete'),
    path('logout/', views.logout_view, name='logout_view'),
]


