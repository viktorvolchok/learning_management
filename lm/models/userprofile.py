from django.db import models

from lm.models import Student


class UserProfile (models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
