from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = "Главная страница"
    context = {
        'title': title,
        'content': 'Главная страница',
    }
    return render(request,template,context)

