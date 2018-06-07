from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 140)
    matricule = models.CharField(max_length = 140)
    level = models.IntegerField()
    password = models.CharField(max_length = 140)
    email = models.CharField(max_length = 140)
    department = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.matricule

class Vote(models.Model):
    user_id = models.IntegerField()
    candidate_id = models.IntegerField()
    date = models.DateTimeField()

class Department(models.Model):
    name = models.IntegerField()
    faculty_id = models.IntegerField()
    date = models.DateTimeField()

class Faculty(models.Model):
    name = models.IntegerField()
    date = models.DateTimeField()

class ElectionSession(models.Model):
    year = models.CharField(max_length = 140)
    expireDate = models.DateTimeField()
    date = models.DateTimeField()

class ElectionType(models.Model):
    name = models.CharField(max_length = 140)
    date = models.DateTimeField()
