from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.

PREFIX_NAME = (
    ("นาย", "นาย"),
    ("นาง", "นาง"),
    ("นางสาว", "นางสาว"),
)


class Student(models.Model):

    prefix_name = models.CharField(max_length=10, choices=PREFIX_NAME, default=1)
    st_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return (
            f"{self.st_id} {self.get_prefix_name_display()} {self.fname} {self.lname}"
        )

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})


class StudentAdmin(admin.ModelAdmin):
    list_display = ("st_id", "get_prefix_name_display", "fname", "lname")


admin.site.register(Student, StudentAdmin)
