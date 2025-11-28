from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.saludo),
    path("hola/", views.hello, name="principal"),
    path("secundario/", views.hola, name="secundario"),
]