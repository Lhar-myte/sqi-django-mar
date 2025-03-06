from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('task/', views.all_task, name="task"),
]