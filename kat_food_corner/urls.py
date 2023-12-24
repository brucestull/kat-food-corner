from django.urls import path

from kat_food_corner import views

app_name = "kat_food_corner"
urlpatterns = [
    path("", views.index, name="index"),
]
