from django.db import models

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