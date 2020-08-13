from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'pages/team/index.html')

def schedule(request):
    return render(request, 'pages/team/calendrier.html')

def our_team(request):
    return render(request, 'pages/team/our-team.html')

def contact(request):
    return render(request, 'pages/team/contact.html')