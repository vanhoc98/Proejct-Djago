from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse

def coming(request):
    return render(request, 'coming.html')