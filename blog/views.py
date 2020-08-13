from django.shortcuts import render

# Create your views here.

def page_home(request):
    return render(request, 'pages/blog/index.html')

def single(request):
    return render(request, 'pages/blog/single.html')

