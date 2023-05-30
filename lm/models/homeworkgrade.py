from django.db import models

from lm.models import Student


class HomeworkGrade(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    grade = models.IntegerField()
