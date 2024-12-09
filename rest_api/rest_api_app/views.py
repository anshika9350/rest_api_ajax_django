from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render

def index(request):
     return render(request, 'index.html')
 
# POST REQUEST
class CreateStudent(APIView):
    def post(self, request, format=None):
        # Deserialize the request data
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save the new student instance to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created student data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# GET REQUEST
class GetStudents(APIView):
    def get(self, request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)

# GET STUDENT BY NAME     
class GetStudentbyName(APIView):
    def get(self, request, name):
        try:
            Students = Student.objects.get(name=name)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(Students)
        return Response(serializer.data)

# DELETE REQUEST    
class DeleteStudentName(APIView):
    def delete(self, request, name, format=None):
        try:
            student = Student.objects.get(name=name)
            student.delete()  # Delete the student
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateStudent(APIView):
    def put(self, request, format=None):
        try:
            Students = Student.objects.all()
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(Students, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class UpdateStudentName(APIView):
    def patch(self,request,name,format=None):
        try:
            Students=Student.objects.get(name=name)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = StudentSerializer(Students, data=request.data, partial=True)
        
        if serializer.is_valid():
           serializer.save()  # Save the changes to the database
           return Response(serializer.data)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  