from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('Sign-Up/', views.signUp , name='signUp'),
    path('Sign-In/', views.signIn , name='signIn'),
    url(r'^sign-up/$', views.signUpForm, name='signUpForm'),
]