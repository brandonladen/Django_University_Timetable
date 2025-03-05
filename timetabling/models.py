from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - ({self.name})"

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    school = models.CharField(max_length=100) #name of room
    lecturer = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=True)
    time_slot = models.CharField(max_length=50, null=True, blank=True)  # e.g., '9:00 AM - 10:00 AM'

    def __str__(self):
        return f"{self.name}"

class AcademicYear(models.Model):
    year = models.CharField(max_length=10)  # e.g., '2023/2024'
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.year

class Year(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='years')
    level = models.IntegerField()  # e.g., 1, 2, 3, 4

    def __str__(self):
        return f"Year {self.level} - {self.academic_year.year}"
    
class TimeSlot(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.instructor} - {self.unit} ({self.day} {self.start_time} - {self.end_time})"
    
class ClassSchedule(models.Model):
    academic_year = models.ForeignKey('AcademicYear', on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    year = models.ForeignKey('Year', on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    lecturer = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - {self.unit} ({self.lecturer})"
