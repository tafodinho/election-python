from django.db import models
from django.contrib.auth.models import User
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
    name = models.CharField(max_length = 140)
    matricule = models.CharField(max_length = 140)
    level = models.IntegerField()
    email = models.CharField(max_length = 140)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateTimeField()

    @receiver(post_save, sender=User)
    def create_user_student(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_student(sender , instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.matricule

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
