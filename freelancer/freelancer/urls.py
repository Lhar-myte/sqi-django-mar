from django.urls import path
from . import views

app_name = "freelancer"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('service/', views.services, name="services"),
    path('blog/', views.blog, name="blog"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('pricing/', views.pricing, name="pricing"),
    path('case_studies/', views.case_studies, name="case_studies"),
]
