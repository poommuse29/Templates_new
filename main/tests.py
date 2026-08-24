from django.test import TestCase
from django.urls import reverse
from .models import Student, Major
from .forms import StudentForm


class StudentCRUDTests(TestCase):

    def setUp(self):
        # Create a major
        self.major = Major.objects.create(mj_name="Computer Science")
        # Create a student
        self.student = Student.objects.create(
            prefix_name="นาย",
            st_id="64010001",
            fname="TestFirst",
            lname="TestLast",
            major=self.major,
        )

    def test_student_form_valid(self):
        form_data = {
            "prefix_name": "นาย",
            "st_id": "64010002",
            "fname": "AnotherFirst",
            "lname": "AnotherLast",
            "major": self.major.id,
        }
        form = StudentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_student_form_invalid_duplicate_id(self):
        form_data = {
            "prefix_name": "นาย",
            "st_id": "64010001",  # Duplicate ID
            "fname": "Duplicate",
            "lname": "User",
            "major": self.major.id,
        }
        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("st_id", form.errors)

    def test_student_list_view(self):
        response = self.client.get(reverse("student_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "64010001")
        self.assertContains(response, "TestFirst")

    def test_student_create_view_get(self):
        response = self.client.get(reverse("student_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "student_form.html")

    def test_student_create_view_post(self):
        data = {
            "prefix_name": "นางสาว",
            "st_id": "64010003",
            "fname": "NewFirst",
            "lname": "NewLast",
            "major": self.major.id,
        }
        response = self.client.post(reverse("student_create"), data)
        self.assertRedirects(response, reverse("student_list"))
        self.assertTrue(Student.objects.filter(st_id="64010003").exists())

    def test_student_update_view_get(self):
        response = self.client.get(
            reverse("student_update", kwargs={"pk": self.student.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "64010001")

    def test_student_update_view_post(self):
        data = {
            "prefix_name": "นาง",
            "st_id": "64010001",
            "fname": "UpdatedFirst",
            "lname": "UpdatedLast",
            "major": self.major.id,
        }
        response = self.client.post(
            reverse("student_update", kwargs={"pk": self.student.pk}), data
        )
        self.assertRedirects(response, reverse("student_list"))
        self.student.refresh_from_db()
        self.assertEqual(self.student.fname, "UpdatedFirst")
        self.assertEqual(self.student.prefix_name, "นาง")

    def test_student_delete_view_get(self):
        response = self.client.get(
            reverse("student_delete", kwargs={"pk": self.student.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "student_confirm_delete.html")

    def test_student_delete_view_post(self):
        response = self.client.post(
            reverse("student_delete", kwargs={"pk": self.student.pk})
        )
        self.assertRedirects(response, reverse("student_list"))
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())

