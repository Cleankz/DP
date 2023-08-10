from django.urls import path, include
from . import views
urlpatterns = [
    path('institutions/', views.InstitutionListView.as_view()),
    path('sensor-data/', views.SensorDataView.as_view()),
    path('login/', views.LoginView.as_view()),
]