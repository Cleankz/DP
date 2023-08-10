from django.urls import path, include

from fcontrol import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authorization/', views.authorization, name='auth'),
    path('registration/', views.registration, name='reg')
]