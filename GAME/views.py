from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index page")

def about(request):
    return HttpResponse("This is the about page")

urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about, name='about'),  
]