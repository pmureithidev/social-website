from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
urlpatterns = [
    # using a single url from auth to handle authentication
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'),
]