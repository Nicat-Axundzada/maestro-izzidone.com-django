from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('reset/', views.password_reset, name='password_reset'),
    path('reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/complete/', views.password_reset_complete,
         name='password_reset_complete'),
    path('reset/<str:token>/', views.password_reset_confirm,
         name='password_reset_confirm'),
]
