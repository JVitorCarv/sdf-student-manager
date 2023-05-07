from django.db import models
from datetime import date

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    tracking = models.URLField(blank=True)
    repo = models.URLField(blank=True)
    prototype = models.URLField(blank=True)
    description = models.TextField(max_length=512, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    grade_1 = models.FloatField(default=0)
    grade_2 = models.FloatField(default=0)
    grade_avg = models.FloatField(default=0)
    presences = models.IntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    description = models.TextField(max_length=2048, blank=True)
    students = models.ManyToManyField('Student', related_name='lesson_presence')

    def __str__(self):
        return f'{self.date} - {self.subject}'
    