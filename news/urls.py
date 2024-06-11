from django.urls import path, include
from .views import home, news_details, categories_form, news_form, Category_ViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', Category_ViewSet)


urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news/", news_form, name="news-form"),
    path("api/", include(router.urls)),
]