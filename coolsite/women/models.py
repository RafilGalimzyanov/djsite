from django.db import models

"""
Описание модели
"""

class Women(models.Model): #Наследуем от базового класса model, поле id прописано в Model
    title = models.CharField(max_length=255) # Текстовое поле длиной до 255
    content = models.TextField(blank=True) # Текст статьи, параметр значит, что поле может быть пустым
    photo = models.ImageField(upload_to='photos/%Y/%n/%d/') # Ссылка на фотографию поста
    time_create = models.DateTimeField(auto_now_add=True) # Время создания, поле не меняется после создания
    time_update = models.DateTimeField(auto_now=True) # Время последнего редактирования статьи, поле будет меняться каждый раз
    is_published = models.BooleanField(default=True) # По умолчанию ставим True

    def __str__(self):
        return self.title #Возвращаем заголовок текущей записи в терминале