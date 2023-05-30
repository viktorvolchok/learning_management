from django.db import models

from lm.models.homework import Homework
from lm.models.lesson import Lesson
from lm.models.student import Student
from lm.models.teacher import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=40, unique=True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    lessons = models.ManyToManyField(Lesson)
    homeworks = models.ManyToManyField(Homework)

    def __str__(self):
        return self.name
