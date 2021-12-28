from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Страница приложегия women.')

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    return HttpResponse(f'archive - {year}')