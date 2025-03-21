from django.db import models

# Create your models here.

class Department(models.Model):
    dpt_name = models.CharField(max_length=255, null=True, blank=True)

def __str__(self):
     return self.dpt_name

class Student(models.Model):
    full_name = models.CharField(max_length=255,)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    no_of_student = models.PositiveBigIntegerField()


def __str__(self):
        return f"{self.full_name} of {self.department} department"