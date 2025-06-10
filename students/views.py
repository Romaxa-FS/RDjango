from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Subject, Grade
from django.db.models import Avg

def home(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    grades = Grade.objects.all()
    return render(request, 'students/home.html', {'students': students, 'subjects': subjects, 'grades': grades})

def add_student(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        Student.objects.create(full_name=full_name)
        return redirect('home')
    return render(request, 'students/add_student.html')

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.full_name = request.POST['full_name']
        student.save()
        return redirect('home')
    return render(request, 'students/edit_student.html', {'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'students/delete_student.html', {'student': student})

def add_subject(request):
    if request.method == 'POST':
        name = request.POST['name']
        Subject.objects.create(name=name)
        return redirect('home')
    return render(request, 'students/add_subject.html')

def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('home')
    return render(request, 'students/delete_subject.html', {'subject': subject})

def add_grade(request):
    if request.method == 'POST':
        student_id = request.POST['student']
        subject_id = request.POST['subject']
        value = request.POST['value']
        Grade.objects.create(student_id=student_id, subject_id=subject_id, value=value)
        return redirect('home')
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'students/add_grade.html', {'students': students, 'subjects': subjects})

def delete_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('home')
    return render(request, 'students/delete_grade.html', {'grade': grade})

def report(request):
    student_averages = Student.objects.annotate(avg_grade=Avg('grade__value'))
    subject_averages = Subject.objects.annotate(avg_grade=Avg('grade__value'))
    best_student = student_averages.order_by('-avg_grade').first()
    worst_student = student_averages.order_by('avg_grade').first()
    return render(request, 'students/report.html', {
        'student_averages': student_averages,
        'subject_averages': subject_averages,
        'best_student': best_student,
        'worst_student': worst_student,
    })