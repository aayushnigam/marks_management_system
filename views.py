# marks/views.py
import csv
from django.shortcuts import render, redirect
from .forms import StudentForm, MarkForm
from .models import Student, Mark
from django.conf import settings
import os

def index(request):
    return render(request, 'index.html')

def student_list(request):
    # Read data from CSV file for student list
    csv_file_path = 'E:\Marks_management_system\marks_project\marks\student_data.csv'
    student_list_data = read_csv_student_list(csv_file_path)

    return render(request, 'student_list.html', {'students': student_list_data})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    # Read data from CSV file for student information
    csv_file_path = 'E:\Marks_management_system\marks_project\marks\student_data.csv'
    student_data = read_csv_student_data(csv_file_path)

    return render(request, 'add_student.html', {'form': form, 'student_data': student_data})

def read_csv_student_data(file_path):
    student_data = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        # Assuming the CSV file has columns 'First Name', 'Last Name', 'Roll Number', 'Subjects', 'Marks', etc.
        first_name_index = header.index('First Name')
        last_name_index = header.index('Last Name')
        roll_number_index = header.index('Roll Number')
        subjects_index = header.index('Subjects')
        marks_index = header.index('Marks')

        for row in csv_reader:
            student_data.append({
                'first_name': row[first_name_index],
                'last_name': row[last_name_index],
                'roll_number': row[roll_number_index],
                'subjects': row[subjects_index],
                'marks': row[marks_index],
            })

    return student_data

def read_csv_student_list(file_path):
    student_list_data = []

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return student_list_data

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        # Assuming the CSV file has columns 'First Name', 'Last Name', 'Roll Number', 'Subjects', 'Marks', etc.
        first_name_index = header.index('First Name')
        last_name_index = header.index('Last Name')
        roll_number_index = header.index('Roll Number')
        subjects_index = header.index('Subjects')
        marks_index = header.index('Marks')

        for row in csv_reader:
            student_list_data.append({
                'first_name': row[first_name_index],
                'last_name': row[last_name_index],
                'roll_number': row[roll_number_index],
                'subjects': row[subjects_index].split(','),  # Split subjects by comma
                'marks': [int(mark.strip()) for mark in row[marks_index].split(',')],  # Split marks by comma and convert to integers
            })

    print(f"Student List Data: {student_list_data}")
    return student_list_data

def marks_list(request):
    marks = Mark.objects.all()

    # Handle form submission
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marks_list')
    else:
        form = MarkForm()

    # Read data from CSV file for charting
    csv_file_path = 'E:\Marks_management_system\marks_project\marks\student_data.csv'
    chart_data = read_csv_data(csv_file_path)

    return render(request, 'marks_list.html', {'marks': marks, 'form': form, 'chart_data': chart_data})

def read_csv_data(file_path):
    chart_data = {'labels': [], 'data': []}

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        # Assuming the CSV file has columns 'Subject' and 'Score'
        name_index = header.index('First Name')
        subject_index = header.index('Subjects')
        score_index = header.index('Marks')

        for row in csv_reader:
            chart_data['labels'].append(row[name_index])
            # Split the 'Score' string into a list of individual scores
            scores = [int(score.strip()) for score in row[score_index].split(',')]
            # Take the average of the scores and append to the 'data' list
            chart_data['data'].append(sum(scores) / len(scores))

    return chart_data

