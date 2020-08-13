from django.urls import path

from . import views

app_name='blog'
urlpatterns = [
    
    path('', views.page_home, name='home'),
    path('single', views.single, name='single'),
    
]