from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import viewsets, authentication, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from election.models import Student, Vote, Department, Faculty, ElectionSession, ElectionType
from election.serializer import UserSerializer, StudentSerializer, VoteSerializer, DepartmentSerializer, FacultySerializer, ElectionSessionSerializer, ElectionTypeSerializer, ElectionTypeSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import ( authenticate, get_user_model, login, logout)

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=False)
    def login(self, request):
        queryset = self.get_queryset()
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"message": username + ' does not exist'})
        else:

            login(request, user)
            # serializer = UserSerializer(user)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def logout(self, request):
        logout(request)
