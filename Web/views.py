from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the home page of my web application!")


def about(request):
    return HttpResponse("This is the about page. Learn more about our web application here!")
