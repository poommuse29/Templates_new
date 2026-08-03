from django.shortcuts import render
from .models import Student
import datetime


def index(request):
    context = {
        "title": "My Home Page",
    }

    students = Student.objects.all()
    context["students"] = students

    context["date"] = datetime.date.today()
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
