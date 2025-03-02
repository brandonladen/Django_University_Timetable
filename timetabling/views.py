from django.shortcuts import render
from django.http import JsonResponse
from .models import School, Department, Course, Unit, Instructor, Room, AcademicYear, Year


def signin(request):
    return render(request, 'timetabling/signin.html')

def signup(request):
    return render(request, 'timetabling/signup.html')

def index(request):
    schools = School.objects.all()
    academic_years = AcademicYear.objects.all()
    years = Year.objects.all()

    context = {
        'schools': schools,
        'academic_years': academic_years,
        'years': years,
    }

    return render(request, 'timetabling/index.html', context)


def get_departments(request):
    school_id = request.GET.get('school_id')
    departments = Department.objects.filter(school_id=school_id).values('id', 'name')
    return JsonResponse(list(departments), safe=False)

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

def get_units(request):
    course_id = request.GET.get('course_id')
    units = Unit.objects.filter(course_id=course_id).values('id', 'name')
    return JsonResponse(list(units), safe=False)
