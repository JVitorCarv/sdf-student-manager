from django.urls import path
from . import views

app_name = 'presence_count'

urlpatterns = [
    path('', views.home, name='home'),
    path('newstudent/', views.register, name='register_student'), 
    path('rollcall/', views.roll_call, name='roll_call'),
    path('grades/', views.grades_manager, name='grades_manager'),
    path('newgroup/', views.register_group, name='register_group'),
    path('student/', views.student, name='student'),
    path('student/<int:student_id>', views.view_student, name='view_student'),
    path('group/<int:group_id>', views.view_group, name='view_group')
]