from django.db import models

from lm.models import Student


class Diploma (models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
