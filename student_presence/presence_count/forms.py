from django import forms
from .models import Group, Lesson, Student


class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'group', 'email')


class RegisterGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class RegisterLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('subject', 'date', 'description')
        widgets = {
            'date': forms.SelectDateWidget()
        }
        