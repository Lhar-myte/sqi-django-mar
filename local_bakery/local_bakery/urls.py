from django.urls import path

from . import views

app_name = "local_bakery"

urlpatterns = [
    path("home/",views.home, name="homepage"),
    path("about/",views.about, name="about-us"),
    path("contact/",views.contact_us, name="contact-us"),
    path("menu/", views.menu, name="menu"),
    path('subscribe/', views.subscribe, name='subscribe'),

]