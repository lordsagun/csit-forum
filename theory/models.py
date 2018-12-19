from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.
class Semester(models.Model):
    semester_name=models.CharField(max_length=50)

    def __str__(self):
        return self.semester_name

class Year(models.Model):
    year=models.CharField(max_length=4,help_text="Use the following format: 2066")

    def __str__(self):
        return self.year

class OldQuestion(models.Model):
    old_question_file=models.FileField(upload_to='old_question/')
    subject=models.CharField(max_length=1000)
    year=models.ForeignKey(Year)
    sem=models.ForeignKey(Semester)

    def __str__(self):
        return self.subject

class Syllabus(models.Model):
    syllabus_file=models.FileField(upload_to='syllabus/')
    subject=models.CharField(max_length=100)
    sem=models.ForeignKey(Semester)

    def __str__(self):
     return self.subject

class Note(models.Model):
    note_file=models.FileField(upload_to='note/')
    subject=models.CharField(max_length=100)
    sem=models.ForeignKey(Semester)

    def __str__(self):
     return self.subject

class Solution(models.Model):
    solution_file=models.FileField(upload_to='solution/')
    subject=models.CharField(max_length=100)
    year=models.ForeignKey(Year)
    sem=models.ForeignKey(Semester)

    def __str__(self):
        return self.subject

class Result(models.Model):
    symbol_number=models.CharField(max_length=20)
    year=models.ForeignKey(Year)
    sem=models.ForeignKey(Semester)

    def __str__(self):
        return self.symbol_number
