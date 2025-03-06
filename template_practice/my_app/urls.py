from django.urls import path
from . import views


app_name = 'my_app'

urlpatterns = [
    path('my_app/', views.welcome, name="my-app"),
]
