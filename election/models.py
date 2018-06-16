from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Faculty(models.Model):
    name = models.CharField(max_length = 140)
    date = models.DateTimeField(auto_now_add=True)

class Department(models.Model):
    name = models.CharField(max_length = 140)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE, )
    name = models.CharField(max_length = 140)
    matricule = models.CharField(max_length = 140)
    level = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Vote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    candidate_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class ElectionSession(models.Model):
    year = models.CharField(max_length = 140)
    expireDate = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)

class ElectionType(models.Model):
    name = models.CharField(max_length = 140)
    date = models.DateTimeField(auto_now_add=True)
