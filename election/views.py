from rest_framework import permissions, status
from django.contrib.auth.models import User
from rest_framework import viewsets, authentication, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from election.models import Student, Vote, Department, Faculty, ElectionSession, ElectionType, Candidate
from election.serializer import UserSerializer, StudentSerializer, VoteSerializer, DepartmentSerializer, CandidateSerializer, FacultySerializer, ElectionSessionSerializer, ElectionTypeSerializer, ElectionTypeSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import ( authenticate, get_user_model, login, logout)
from rest_framework.renderers import JSONRenderer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    @action(methods=['get'], detail=False)
    def result(self, request):
        candidates = Candidate.objects.all()
        result = []

        for candidate in candidates:
            vote = Vote.objects.filter(candidate__id=candidate.id).count()
            result.append({
                "id": candidate.id,
                "name": candidate.student.name,
                "vote": vote,
                "level": candidate.student.level,
                "department": candidate.student.department.name,
                "matricule": candidate.student.matricule,
                "position": candidate.position
            })
        result.sort(key=lambda x: int(x["vote"]), reverse=True)
        return Response(result)

    @action(methods=['get'], detail=False)
    def candidates(self, request):
        try:
            print(request.query_params['position'])
            data = request.query_params['position']
            candidates = Candidate.objects.filter(position=data)
            result = []
            for candidate in candidates:
                vote = Vote.objects.filter(candidate__id=candidate.id).count()
                result.append({
                    "id": candidate.id,
                    "name": candidate.student.name,
                    "vote": vote,
                    "level": candidate.student.level,
                    "department": candidate.student.department.name,
                    "matricule": candidate.student.matricule,
                    "position": candidate.position
                })
            result.sort(key=lambda x: int(x["vote"]), reverse=True)
            return Response(result)
        except Exception as e:
            return Response({"error": e.args})


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

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # renderer_classes = (JSONRenderer, )

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
            return Response({'message': 'incorrect credentials'}, status=status.HTTP_404_NOT_FOUND)
        else:
            login(request, user)
            # serializer = UserSerializer(user)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def logout(self, request):
        logout(request)
        return Response({"message": "Logout Success"}, status=status.HTTP_201_CREATED)
