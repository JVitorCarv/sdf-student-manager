from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'presence_count'

urlpatterns = [
    path('', views.home, name='home'),
    path('student/add/', views.register, name='register_student'), 
    path('lesson/', views.roll_call, name='lesson'),
    path('lesson/all/', views.lesson_manager, name='lesson_manager'),
    path('lesson/edit/<int:lesson_id>', views.edit_lesson, name='edit_lesson'),
    path('lesson/confirm_delete/<int:lesson_id>', views.confirm_delete_lesson, name='confirm_delete_lesson'),
    path('lesson/delete/<int:lesson_id>', views.delete_lesson, name='delete_lesson'),
    path('grades/', views.grades_manager, name='grades_manager'),
    path('newgroup/', views.register_group, name='register_group'),
    path('student/', views.student, name='student'),
    path('student/<int:student_id>', views.view_student, name='view_student'),
    path('student/edit/<int:student_id>', views.edit_student, name='edit_student'),
    path('student/confirm_delete/<int:student_id>', views.confirm_delete_student, name='confirm_delete_student'),
    path('student/delete/<int:student_id>', views.delete_student, name='delete_student'),
    path('student/select/', views.select_student, name='select_student'),
    path('group/', views.group, name='group'),
    path('group/select/', views.select_group, name='select_group'),
    path('group/edit/<int:group_id>', views.edit_group, name='edit_group'),
    path('group/confirm_delete/<int:group_id>', views.confirm_delete_group, name='confirm_delete_group'),
    path('group/delete/<int:group_id>', views.delete_group, name='delete_group'),
    path('group/<int:group_id>', views.view_group, name='view_group'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)