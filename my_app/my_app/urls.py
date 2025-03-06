from django.urls import path
from . import views


urlpatterns = [
    path('my-app/', views.my_app, name="my-app"),
]


