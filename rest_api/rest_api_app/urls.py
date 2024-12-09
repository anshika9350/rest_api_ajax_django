from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('student', views.GetStudents.as_view(), name='get-student'),
    path('create_student',views. CreateStudent.as_view(),name='create-student'),
    path('student/<str:name>/', views.GetStudentbyName.as_view(), name='get-student-name'),
    path('update/', views.UpdateStudent.as_view(), name='update-student'),
    path('update/<str:name>',views.UpdateStudentName.as_view(),name='update-student-name'),
    path('student/<str:name>/delete',views.DeleteStudentName.as_view(),name='delete-student')
]

