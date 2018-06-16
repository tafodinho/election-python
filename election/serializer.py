from election.models import Student, Vote, Department, Faculty, ElectionSession, ElectionType
from django.contrib.auth.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'matricule', 'level', 'department', 'date')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

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
class UserSerializer(serializers.ModelSerializer):
    student = StudentSerializer(required=True)

    class Meta:
        model = User
        fields = ('id','username', 'password', 'student', 'email')

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        user = User.objects.create(
            **validated_data
        )
        print(user)
        student = Student.objects.create(
            user = user, **student_data
        )

        return user
