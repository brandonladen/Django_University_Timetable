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
    code = models.CharField(max_length=10, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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
    lecturer = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=50)  # e.g., '9:00 AM - 10:00 AM'

    def __str__(self):
        return f"{self.unit.name} - {self.time_slot} in {self.room}"

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
