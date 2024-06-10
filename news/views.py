from django.shortcuts import redirect, render
from .models import News, Category, CategoryForm


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