from django import forms
from .models import Student,Mark

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'marks']

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['subject', 'score']