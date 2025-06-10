from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/add/', views.add_student, name='add_student'),
    path('student/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('subject/add/', views.add_subject, name='add_subject'),
    path('subject/delete/<int:pk>/', views.delete_subject, name='delete_subject'),
    path('grade/add/', views.add_grade, name='add_grade'),
    path('grade/delete/<int:pk>/', views.delete_grade, name='delete_grade'),
    path('report/', views.report, name='report'),
]