

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# from school.models import Student
from school.models import Clasroom
from school.models import Student


def index(request):
    clasrooms = Clasroom.objects.all()
    context = {

        'data' : clasrooms
    }
    return render(request, 'school/index.html', context)



def students(request):
    students = Student.objects.all()
    context = {

        'data' : students
    }
    return render(request, 'school/students.html', context)


def clasrooms(request):
    classrooms = Clasroom.objects.all()
    
    context = {

        'data' : classrooms
    }
    return render(request, 'school/classrooms.html', context)


def show_by_class_page(request, classroom_id):
    classroom_selected = Clasroom.objects.get(id = classroom_id)
    students_by_classroom = Student.objects.filter(clasroom = classroom_selected)
    print(students_by_classroom)
    context = {
            "classroom_selected" : classroom_selected,
            "students_by_classroom" : students_by_classroom
    }

    return render( request, 'school/classroom_selected.html', context)




