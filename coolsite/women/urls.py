from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('cats/<int:catid>/', categories),
    path('about/', about, name='about'),
    re_path(r'^archive/(?P<year>[0-8]{4})/', archive)
]