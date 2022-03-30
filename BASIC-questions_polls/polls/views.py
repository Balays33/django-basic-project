from django.shortcuts import render
from django.http import HttpResponse

from django.http import Http404
#import requests

"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
"""


# Create your views here.
#index page view
def index(request):
    print("index page")
    return render(request, 'polls/index.html' )