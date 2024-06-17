from . import views
from django.urls import path

urlpatterns = [
    path('', views.users, name='users'),
    path('register/', views.register, name='register'),

]
