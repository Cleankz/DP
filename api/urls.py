from django.urls import path, include

urlpatterns = [
    path('fcontrol/' , include('api.fcontrol.urls'))
]