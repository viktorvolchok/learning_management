from rest_framework import serializers

from lm.models import Subject, Student, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "name")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "name")


class SubjectSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    teacher = TeacherSerializer()

    class Meta:
        model = Subject
        fields = ("id", "name", "students", "teacher")
