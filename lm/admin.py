from django.contrib import admin

# Register your models here.
from lm.models import Subject, Teacher, Student, Lesson, Homework

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Homework)
