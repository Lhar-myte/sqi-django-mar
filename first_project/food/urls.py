from django.urls import path
from . import views


urlpatterns = [
    path('our-menu/', views.menu, name="home"),
    path('contact-us/', views.contact, name="contact"),
]