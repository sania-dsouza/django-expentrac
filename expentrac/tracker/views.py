from django.shortcuts import render


def base_page(request):
    return render(request, 'tracker/base.html')

