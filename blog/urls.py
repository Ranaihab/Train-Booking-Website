from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Sign-Up/', views.signUp , name='signUp'),
    path('Sign-In/', views.signIn , name='signIn')
]