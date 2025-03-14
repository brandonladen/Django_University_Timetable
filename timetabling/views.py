from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import School, Department, Course, Unit, Instructor, Room, AcademicYear, Year, ClassSchedule, TimeSlot


def signin(request):
    return render(request, 'timetabling/signin.html')

def signup(request):
    return render(request, 'timetabling/signup.html')

def index(request):
    schools = School.objects.all()
    academic_years = AcademicYear.objects.all()
    years = Year.objects.all()
    instructor = Instructor.objects.all()

    context = {
        'schools': schools,
        'academic_years': academic_years,
        'years': years,
        'instructor' : instructor
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

def get_instructors_by_unit(request, unit_id):
    instructors = Instructor.objects.filter(timeslot__unit_id=unit_id).distinct()
    instructor_data = [{'id': instructor.id, 'name': f"{instructor.first_name} {instructor.last_name}"} for instructor in instructors]
    return JsonResponse({'instructors': instructor_data})

@csrf_exempt
def create_class_schedule(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            academic_year = data.get("academic_year")
            semester = data.get("semester")
            school_id = data.get("school")
            department_id = data.get("department")
            course_id = data.get("course")
            year = data.get("year")
            unit_id = data.get("unit")
            lecturer_id = data.get("lecturer")

            # Ensure required fields exist
            if not all([academic_year, semester, school_id, department_id, course_id, year, unit_id, lecturer_id]):
                return JsonResponse({"error": "Missing required fields"}, status=400)

            school = get_object_or_404(School, id=school_id)
            department = get_object_or_404(Department, id=department_id)
            course = get_object_or_404(Course, id=course_id)
            unit = get_object_or_404(Unit, id=unit_id)
            lecturer = get_object_or_404(Instructor, id=lecturer_id)

            # Save ClassSchedule
            schedule = ClassSchedule.objects.create(
                academic_year=academic_year,
                semester=semester,
                school=school,
                department=department,
                course=course,
                year=year,
                unit=unit,
                lecturer=lecturer
            )

            return JsonResponse({"message": "Class schedule created successfully", "schedule_id": schedule.id})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_class_schedules(request):
    schedules = ClassSchedule.objects.all()
    schedule_list = []

    for schedule in schedules:
        # Fetch corresponding timeslot
        timeslot = TimeSlot.objects.filter(instructor=schedule.lecturer, unit=schedule.unit).first()
        timeslot_data = {
            "day": timeslot.day if timeslot else "Not Assigned",
            "start_time": timeslot.start_time.strftime("%H:%M") if timeslot else "N/A",
            "end_time": timeslot.end_time.strftime("%H:%M") if timeslot else "N/A",
        } if timeslot else {}

        schedule_list.append({
            "id": schedule.id,
            "academic_year": schedule.academic_year,
            "semester": schedule.semester,
            "school": schedule.school.name,
            "department": schedule.department.name,
            "course": schedule.course.name,
            "year": schedule.year,
            "unit": schedule.unit.name,
            "lecturer": schedule.lecturer.name,
            "timeslot": timeslot_data
        })

    return JsonResponse({"schedules": schedule_list})


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ClassSchedule

def save_class(request):
    if request.method == "POST":
        academic_year = request.POST.get("academicYear")
        semester = request.POST.get("semester")
        school = request.POST.get("school")
        department = request.POST.get("department")
        course = request.POST.get("course")
        year = request.POST.get("year")
        unit = request.POST.get("unit")
        lecturer = request.POST.get("lecturer")

        # Validate required fields
        if not all([academic_year, semester, school, department, course, year, unit, lecturer]):
            return JsonResponse({"error": "All fields are required"}, status=400)

        # Save to ClassSchedule model
        class_schedule = ClassSchedule.objects.create(
            academic_year_id=academic_year,
            semester=semester,
            school_id=school,
            department_id=department,
            course_id=course,
            year_id=year,
            unit_id=unit,
            lecturer_id=lecturer
        )
        class_schedule.save()

        return render(request, "timetabling/index.html")
    return JsonResponse({"error": "Invalid request"}, status=400)

def class_timetable(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Check if request is AJAX
        timetable_data = {}

        # Fetch the current academic year (ensure your model has this field)
        current_academic_year = AcademicYear.objects.filter(is_active=True).first()
        academic_year_str = current_academic_year.year if current_academic_year else "Cannot fetch data"

        # Fetch all scheduled classes
        class_schedules = ClassSchedule.objects.all()

        for schedule in class_schedules:
            dept_name = schedule.department.name  # Group by department
            year_name = f"Year {schedule.year.level}"  # Group by academic year (e.g., Year 1, Year 2)

            if dept_name not in timetable_data:
                timetable_data[dept_name] = {}

            if year_name not in timetable_data[dept_name]:
                timetable_data[dept_name][year_name] = {}

            time_slots = TimeSlot.objects.filter(unit=schedule.unit, instructor=schedule.lecturer)

            for slot in time_slots:
                day = slot.day
                start_hour = slot.start_time.hour  
                end_hour = slot.end_time.hour  

                if day not in timetable_data[dept_name][year_name]:
                    timetable_data[dept_name][year_name][day] = {}

                for hour in range(start_hour, end_hour):  
                    timetable_data[dept_name][year_name][day][hour] = {
                        "unit": schedule.unit.code,
                        "unitname": schedule.unit.name,
                        "course": schedule.course.name,
                        "instructor": f"{schedule.lecturer.first_name} {schedule.lecturer.last_name}"
                    }

        return JsonResponse({"timetable_data": timetable_data, "academic_year_str": academic_year_str})

    return render(request, "timetabling/index.html")

