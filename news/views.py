from django.shortcuts import render
from .models import News


def home(request):
    content = {"news": News.objects.all()}
    return render(request, "home.html", content)


def news_details(request, id):
    content = {"news": News.objects.get(id=id)}
    return render(request, 'news_details.html', content)