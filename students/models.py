from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField()
