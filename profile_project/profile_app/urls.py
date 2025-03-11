from django.urls import path

from . import views


app_name = "profile_app"

urlpatterns = [
    path("", views.index, name = "index"),
    path("goals/", views.goals, name = "goals"),
    path("hobbies/", views.hobbies, name = "hobbies"),
]