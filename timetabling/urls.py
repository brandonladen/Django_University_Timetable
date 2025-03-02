from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("signin",views.signin, name="signin"),
    path("signup",views.signup, name="signup"),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('get_units/', views.get_units, name='get_units'),
    ]