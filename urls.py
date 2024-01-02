# marks/urls.py
from django.urls import path
from .views import index, student_list, marks_list, add_student

urlpatterns = [
    path('', index, name='index'),
    path('students/', student_list, name='student_list'),
    path('marks/', marks_list, name='mark_list'),
    path('addstudent/', add_student, name='add_student'),
]
