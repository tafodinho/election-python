from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import viewsets, authentication, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from election.models import Student, Vote, Department, Faculty, ElectionSession, ElectionType
from election.serializer import StudentSerializer, VoteSerializer, DepartmentSerializer, FacultySerializer, ElectionSessionSerializer, ElectionTypeSerializer, ElectionTypeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class ElectionSessionViewSet(viewsets.ModelViewSet):
    queryset = ElectionSession.objects.all()
    serializer_class = ElectionSessionSerializer

class ElectionTypeViewSet(viewsets.ModelViewSet):
    queryset = ElectionType.objects.all()
    serializer_class = ElectionTypeSerializer
