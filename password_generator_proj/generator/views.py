from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'testDictionary':'testDictInfo'})

def example(request):
    return HttpResponse('This is the new example page!')
