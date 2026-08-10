from django.shortcuts import render
from .models import Student, Major
import datetime


def index(request):
    context = {
        "title": "Home page",
    }

    students = Student.objects.filter(major__mj_name__contains="วิทยาการคอมพิวเตอร์")
    context["students"] = students

    context["date"] = datetime.date.today()
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {"student": student}
    return render(request, "student_detail.html", context)


def major_list(request):
    context = {
        "majors": Major.objects.all(),
    }
    return render(request, "major_list.html", context)
