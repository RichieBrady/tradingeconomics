from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_categories/", views.get_categories_list, name="get_categories"),
    path("get_countries/", views.get_countries_list, name="get_countries"),
    path("get_data/", views.get_data, name="get_data")
]
