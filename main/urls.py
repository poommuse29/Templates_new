from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("major/", views.major_list, name="major_list"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("students/", views.student_list, name="student_list"),
    path("student/add/", views.student_create, name="student_create"),
    path("student/<int:pk>/edit/", views.student_update, name="student_update"),
    path("student/<int:pk>/delete/", views.student_delete, name="student_delete"),
]

