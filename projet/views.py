from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    data = {'titre':'petit monsieur', 'label':'tapette'}
    return render(request, 'index.html', data)