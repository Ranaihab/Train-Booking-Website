from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('Sign-Up/', views.signUp , name='signUp'),
    path('Sign-In/', views.signIn , name='signIn'),
    url(r'^sign-up/$', views.signUpForm, name='signUpForm'),
    url(r'^login/$', views.signInForm, name='signInForm'),
    url(r'^logout/$', views.logOut, name='logOut'),
    url('updateProfile/<username>', views.updateProfile, name='updateProfile'),
    url('profile', views.profile, name='profile')
]