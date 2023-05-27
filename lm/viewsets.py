from rest_framework.viewsets import ModelViewSet

from lm.models import Subject, Student
from lm.serializers import SubjectSerializer, StudentSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all().select_related('teacher').prefetch_related('students')
    serializer_class = SubjectSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
