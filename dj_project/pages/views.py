from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageViev(request):
    return HttpResponse("Hello, World!")