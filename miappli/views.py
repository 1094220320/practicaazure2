from django.shortcuts import render
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("hola que tal")

def hello(request):
    return render(request,"anime.html")

def hola(request):
    return render(request,"1-plantilla.html")