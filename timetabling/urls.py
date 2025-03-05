from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("signin",views.signin, name="signin"),
    path("signup",views.signup, name="signup"),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('get_units/', views.get_units, name='get_units'),
    path('get-instructors/<int:unit_id>/', views.get_instructors_by_unit, name='get_instructors_by_unit'),
    path('create_schedule/', views.create_class_schedule, name='create_schedule'),
    path('get_schedules/', views.get_class_schedules, name='get_schedules'),
    path("save-class/", views.save_class, name="save_class"),
    path("timetable/", views.class_timetable, name="class_timetable"),
    ]