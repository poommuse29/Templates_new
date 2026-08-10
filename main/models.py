from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.

PREFIX_NAME = (
    ("นาย", "นาย"),
    ("นาง", "นาง"),
    ("นางสาว", "นางสาว"),
)


class Major(models.Model):
    mj_name = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.mj_name

    def get_absolute_url(self):
        return reverse("major_detail", kwargs={"pk": self.pk})


class Student(models.Model):

    prefix_name = models.CharField(max_length=10, choices=PREFIX_NAME, default=1)
    st_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return (
            f"{self.st_id} {self.get_prefix_name_display()} {self.fname} {self.lname}"
        )

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "st_id",
        "get_prefix_name_display",
        "fname",
        "lname",
    )


class MajorAdmin(admin.ModelAdmin):
    list_display = ("mj_name",)


admin.site.register(Student, StudentAdmin)
admin.site.register(Major, MajorAdmin)
