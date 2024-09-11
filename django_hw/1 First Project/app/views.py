from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os

def home_view(request):
    pages = {
        'Домашняя страница': '/',
        'Текущее время': '/current_time/',
        'Содержимое рабочей директории': '/workdir/'
    }
    
    context = {
        'pages': pages
    }
    return render(request, 'app/home.html', context)

def current_time_view(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f'Текущее время: {current_time}')

def workdir_view(request):
    workdir = os.listdir(os.getcwd())
    workdir_list = '<br>'.join(workdir)
    return HttpResponse(f'Содержимое рабочей директории:<br>{workdir_list}')
