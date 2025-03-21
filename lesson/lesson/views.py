from django.shortcuts import render, get_object_or_404
from .models import Department,Student


# Create your views here.

def department(request):
    departments = Department.objects.all()
    return render(request, "lesson/department.html", {"departments": departments})

def student(request):
    students = Student.objects.all()
    return render(request, "lesson/student.html", {"students": students})


def student_detail(request, student_id):
    st_details = get_object_or_404(Student, id = student_id)
    return render(request,"lesson/student_details.html", {"st_details": st_details})

def department_detail(request, department_id):
    dpt_details = get_object_or_404(Department, id = department_id)
    return render(request, "lesson/department_details.html", {"dpt_details": dpt_details})