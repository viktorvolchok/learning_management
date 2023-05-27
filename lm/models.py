from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Lesson(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Homework(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=40, unique=True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    lessons = models.ManyToManyField(Lesson)
    homeworks = models.ManyToManyField(Homework)

    def __str__(self):
        return self.name
