from django.urls import path
from . import views

app_name = 'lesson'

urlpatterns = [
    path("department/", views.department, name="department"),
    path("student/", views.student, name="student"),
    path("student_details/<int:student_id>", views.student_detail, name="student_details"),
    path("department_details/<int:department_id>", views.department_detail, name="department_details"),
]