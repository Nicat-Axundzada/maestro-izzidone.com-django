from django.urls import path
from . import views

app_name = 'Services'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<str:service_name>/', views.services, name='services'),
    path('create/', views.create_service,
         name='create_service'),

]
