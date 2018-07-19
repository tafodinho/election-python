from election.models import Student, Vote, Department, Faculty, ElectionSession, ElectionType, Candidate
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'matricule', 'level', 'department', 'date')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class ElectionSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionSession
        fields = '__all__'

class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionType
        fields = '__all__'

class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class CandidateSerializer(serializers.ModelSerializer):
    student = StudentSerializer(required=False)

    class Meta:
        model = Candidate
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    student = StudentSerializer(required=True)

    class Meta:
        model = User
        fields = ('id','username', 'password', 'student', 'email', 'is_staff')

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            password = make_password(validated_data['password'])
        )
        print(user)
        student = Student.objects.create(
            user = user, **student_data
        )

        return user
