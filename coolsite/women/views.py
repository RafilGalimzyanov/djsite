from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *
menu = ["О сайте", "Добавить новую статью", "Обратная связь", "Войти", "Авторизоваться"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu ,'title': 'Главная страница'}) #Второй параметр -- путь к шаблону, путь такой, потому что Django сам ищет в templates
                                                                            # Третий параметр - параметр, передаваемый шаблонам. Словари
def categories(request, catid):
    if(request.GET):
        print(f'Вывод GET запроса ', request.GET)
    return HttpResponse(f'<h1>Статьии по категориям</h1><p>{catid}</p>')

def about(request):
    return render(request, 'women/about.html', {'menu': menu ,'title': 'О сайтее'})

def archive(request, year):
    if int(year) > 250:
        return redirect('home', permanent=True)
    return HttpResponse(f'archive - {year}')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена </h1>')