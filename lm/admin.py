from django.contrib import admin

# Register your models here.
from lm.models import Subject, Teacher, Student, Lesson, Homework, Notification, TeacherProfile, UserProfile, \
    HomeworkGrade, Diploma

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Homework)
admin.site.register(Notification)
admin.site.register(TeacherProfile)
admin.site.register(UserProfile)
admin.site.register(HomeworkGrade)
admin.site.register(Diploma)
