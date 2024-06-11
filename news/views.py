from django.shortcuts import redirect, render
from .models import News, Category, CategoryForm, NewsForm, User
from rest_framework import viewsets
from .serializers import CategorySerializer, UserSerializer, NewsSerializer


def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)


def categories_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home-page")
    else:
        form = CategoryForm()

    return render(request, "categories_form.html", {"form": form})


def news_form(request):
    categories = Category.objects.all()
    news_authors = User.objects.all()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("home-page")
    else:
        form = NewsForm()
    
    news_context = {
        "form": form,
        "categories": categories,
        "authors": news_authors
    }

    return render(request, "news_form.html", news_context)


class Category_ViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class News_ViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer