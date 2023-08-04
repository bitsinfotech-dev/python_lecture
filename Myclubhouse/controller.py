from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    
    return render(request, "home.html",{"fruits":["banana","apple","orange"]});
def services(request):
    return HttpResponse("services");
def about(request):
    return HttpResponse("about");
def contact(request):
    return HttpResponse("contact");