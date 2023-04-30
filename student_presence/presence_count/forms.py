from django import forms
from .models import Group, Student


class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'group', 'email')


class RegisterGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'