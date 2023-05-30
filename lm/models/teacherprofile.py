from django.db import models

from lm.models import Teacher


class TeacherProfile (models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
