
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('experience/',views.experience, name='experience'),   
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume,name='resume'),
]