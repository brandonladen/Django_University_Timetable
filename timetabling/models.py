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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AcademicYear(models.Model):
    year = models.CharField(max_length=10)  # e.g., '2023/2024'
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.year

class Year(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    level = models.IntegerField()  # e.g., 1, 2, 3, 4

    def __str__(self):
        return f"Year {self.level} - {self.academic_year.year}"
