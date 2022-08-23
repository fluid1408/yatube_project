from django.shortcuts import render


# Create your views here.
# Главная страница
def index(request):
    template = "posts/index.html"
    return render(request, template)


# Страница со списком мороженого
def group_posts(request, slug):
    template = "posts/group_list.html"
    return render(request, template)


