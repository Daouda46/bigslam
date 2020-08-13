from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home_page, name='home'),
    path('calendrier', views.schedule, name='shedule'),
    path('our-team', views.our_team, name='our_team'),
    path('contact', views.contact, name='contact'),
]