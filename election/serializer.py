from election.models import Student, Vote, Department, Faculty, ElectionSession, ElectionType
from django.contrib.auth.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

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
