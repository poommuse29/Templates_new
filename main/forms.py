from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["prefix_name", "st_id", "fname", "lname", "major"]
        widgets = {
            "prefix_name": forms.Select(attrs={"class": "form-select"}),
            "st_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "เช่น 640112345"}),
            "fname": forms.TextInput(attrs={"class": "form-control", "placeholder": "เช่น สมชาย"}),
            "lname": forms.TextInput(attrs={"class": "form-control", "placeholder": "เช่น ใจดี"}),
            "major": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "prefix_name": "คำนำหน้าชื่อ (Prefix)",
            "st_id": "รหัสนักศึกษา (Student ID)",
            "fname": "ชื่อจริง (First Name)",
            "lname": "นามสกุล (Last Name)",
            "major": "สาขาวิชา (Major)",
        }
