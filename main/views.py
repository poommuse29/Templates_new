from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Major
from .forms import StudentForm
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
    student = get_object_or_404(Student, pk=pk)
    context = {"student": student}
    return render(request, "student_detail.html", context)


def major_list(request):
    context = {
        "majors": Major.objects.all(),
    }
    return render(request, "major_list.html", context)


def student_list(request):
    students = Student.objects.all()
    context = {
        "title": "รายชื่อนักศึกษา (Student List)",
        "students": students,
    }
    return render(request, "student_list.html", context)


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(
                request,
                f"เพิ่มนักศึกษา {student.fname} {student.lname} สำเร็จเรียบร้อยแล้ว!",
            )
            return redirect("student_list")
        else:
            messages.error(
                request, "เกิดข้อผิดพลาดในการบันทึกข้อมูล กรุณาตรวจสอบอีกครั้ง"
            )
    else:
        form = StudentForm()

    context = {
        "title": "เพิ่มข้อมูลนักศึกษา (Add Student)",
        "form": form,
        "is_create": True,
    }
    return render(request, "student_form.html", context)


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"แก้ไขข้อมูลนักศึกษา {student.fname} {student.lname} สำเร็จเรียบร้อยแล้ว!",
            )
            return redirect("student_list")
        else:
            messages.error(
                request, "เกิดข้อผิดพลาดในการบันทึกข้อมูล กรุณาตรวจสอบอีกครั้ง"
            )
    else:
        form = StudentForm(instance=student)

    context = {
        "title": "แก้ไขข้อมูลนักศึกษา (Edit Student)",
        "form": form,
        "student": student,
        "is_create": False,
    }
    return render(request, "student_form.html", context)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        name = f"{student.fname} {student.lname}"
        student.delete()
        messages.success(
            request, f"ลบข้อมูลนักศึกษา {name} สำเร็จเรียบร้อยแล้ว!"
        )
        return redirect("student_list")

    context = {
        "title": "ยืนยันการลบข้อมูลนักศึกษา (Delete Student)",
        "student": student,
    }
    return render(request, "student_confirm_delete.html", context)

