from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse('Страница приложения women.')

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'archive - {year}')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')