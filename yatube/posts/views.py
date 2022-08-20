from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Главная страница
def index(request):
    template = "index.html"
    return render(request, template)


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Публикация постов')
