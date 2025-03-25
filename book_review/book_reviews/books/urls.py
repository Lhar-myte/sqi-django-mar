from django.urls import path
from . import views

app_name = 'books'


urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('book/<int:book_id>/add_review/', views.add_review, name='add_review'),
    path("django_manual_form/<int:book_id>",views.django_manual_form, name = "django_manual_form"),
    path("update_review_with_model_form/<int:review_id>/",views.update_review_with_model_form, name="update_review_with_model_form"),
    path("confirm_delete_review/<int:review_id>/", views.confirm_delete_review, name="confirm_delete_review"),
    path('delete_review/<int:review_id>/', views.delete_review, name="delete_review"),
]
