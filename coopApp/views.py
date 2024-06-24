from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.http import HttpResponse
from ccop import indexx

def index(request):
    now = datetime.now()
    html = indexx
    return HttpResponse(html)