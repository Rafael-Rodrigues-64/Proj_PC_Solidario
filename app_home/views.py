from django.shortcuts import render


def home(request):
    return render(request, 'app_home/pages/index.html')

def app_home(request):
    return render(request, 'app_home/pages/index.html')

