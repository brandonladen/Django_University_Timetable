from django.shortcuts import render
from .models import School, Department, Course, Unit, Instructor, Room, AcademicYear, Year


def signin(request):
    return render(request, 'timetabling/signin.html')

def signup(request):
    return render(request, 'timetabling/signup.html')

def index(request):
    schools = School.objects.all()
    departments = Department.objects.all()
    courses = Course.objects.all()
    units = Unit.objects.all()
    instructors = Instructor.objects.all()
    rooms = Room.objects.all()
    academic_years = AcademicYear.objects.all()
    years = Year.objects.all()

    context = {
        'schools': schools,
        'departments': departments,
        'courses': courses,
        'units': units,
        'instructors': instructors,
        'rooms': rooms,
        'academic_years': academic_years,
        'years': years,
    }

    return render(request, 'timetabling/index.html', context)
