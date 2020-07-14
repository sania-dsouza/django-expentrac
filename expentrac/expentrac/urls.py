from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('tracker.urls')),   # gave the path no app name, like /tracker/ as the tracker is the only app for the time being
    path('admin/', admin.site.urls),
]

handler404 = 'tracker.views.page_not_found'

handler500 = 'tracker.views.no_resource'
