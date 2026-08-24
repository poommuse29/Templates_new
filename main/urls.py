from django.urls import path
from django.contrib.auth import views as auth_views
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
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]
