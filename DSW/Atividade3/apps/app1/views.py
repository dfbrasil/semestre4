from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#   return HttpResponse("Hello World!")

def index(request):
    return render(request, 'app1/index.html')

def detalhes(request):
    return render(request, 'app1/detalhes.html')