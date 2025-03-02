from django.contrib import admin
from .models import Department, School, AcademicYear, Course, Year, Unit, Room, Instructor
# Register your models here.

admin.site.register(Department)
admin.site.register(School)
admin.site.register(AcademicYear)
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(Unit)
admin.site.register(Room)
admin.site.register(Instructor)