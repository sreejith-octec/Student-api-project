from django.shortcuts import render
from .serializers import StudentSerializer, MarkSerializer
from rest_framework.decorators import api_view
from .models import Student, Mark
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def get_post_students(request):
    """list and create student details"""

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'roll_number': request.data.get('roll_number'),
            'date_of_birth': request.data.get('date_of_birth'),
        }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['GET', 'POST'])
def get_post_marks(request):
    """list and create marks details"""

    if request.method == 'GET':
        marks = Mark.objects.all()
        serializer = MarkSerializer(marks, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'mark': request.data.get('mark'),
            'student': request.data.get('student')
        }
        
        serializer = MarkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_grade(scores):
    """gives number of students in each grade"""

    student_having_A_grade = 0
    student_having_B_grade = 0
    student_having_C_grade = 0
    student_having_D_grade = 0
    student_having_E_grade = 0
    student_having_F_grade = 0

    for score in scores:
        
        if 91 <= score <= 100:
            student_having_A_grade += 1
        elif 81 <= score <= 90:
            student_having_B_grade += 1
        elif 71 <= score <= 80:
            student_having_C_grade += 1
        elif 61 <= score <= 70:
            student_having_D_grade += 1
        elif 55 <= score <= 60:
            student_having_E_grade += 1
        else:
            student_having_F_grade += 1

    grades = ['A', 'B', 'C', 'D', 'E', 'F']
    count_values = [student_having_A_grade, student_having_B_grade, student_having_C_grade,
                    student_having_D_grade, student_having_E_grade, student_having_F_grade]

    grade_letter_count_dict = { K:V for (K,V) in zip(grades, count_values)}

    return grade_letter_count_dict


@api_view(['GET'])
def get_results(request):
    """list students performance"""
    
    if request.method == 'GET':
        marks = Mark.objects.all()
        serializer = MarkSerializer(marks, many=True)
        total_number_of_students = marks.count()
        total_marks = []
        for item in range(0, total_number_of_students): 
            data = marks[item].mark
            total_marks.append(data)
        grade_category_count_dict = get_grade(total_marks)

        distinction_percentage = grade_category_count_dict['A']/ total_number_of_students

        first_class_percentage = (grade_category_count_dict['B'] + grade_category_count_dict['C'])/ total_number_of_students

        pass_percentage = ( total_number_of_students - grade_category_count_dict['F'])/ total_number_of_students


        message = f'Distinction Percentage: {distinction_percentage}         ' \
                  f'First Class Percentage: {first_class_percentage}         ' \
                  f'Pass Percentage: {pass_percentage}'

        return Response({'message': message})



