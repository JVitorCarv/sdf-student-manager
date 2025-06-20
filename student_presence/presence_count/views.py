from django.shortcuts import redirect, render
from presence_count.forms import RegisterGroupForm, RegisterLessonForm, RegisterStudentForm
from .models import Group, Lesson, Student
from django.db.models import F


GRADE_LIMIT = 2.0


# Create your views here.
def home(request):
    return render(request, 'index.html')


def register(request):
    form = RegisterStudentForm()
    if request.method == 'POST':
        print(request.POST)
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Error while saving student')
        return redirect('presence_count:register_student')
    context = {'form': form}
    return render(request, 'student/register_student.html', context)



def register_group(request):
    form = RegisterGroupForm()
    if request.method == 'POST':
        print(request.POST)
        form = RegisterGroupForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Error while saving group')
        return redirect('presence_count:register_group')
    context = {'form': form}
    return render(request, 'group/register_group.html', context)


def roll_call(request):
    student_list = Student.objects.all().order_by('group_id')
    lesson_form = RegisterLessonForm()
    if request.method == 'POST':
        lesson_data = request.POST.copy()
        if 'boxes' in lesson_data:
            del lesson_data['boxes']
        lesson_form = RegisterLessonForm(lesson_data)
        if lesson_form.is_valid():
            created_lesson = lesson_form.save()
        else:
            print('Error while saving lesson_form')
        current_lesson = Lesson.objects.get(pk=created_lesson.id)

        id_list = request.POST.getlist('boxes')
        for student_id in id_list:
            Student.objects.filter(pk=int(student_id)).update(presences=F('presences')+1)
            student = Student.objects.get(pk=int(student_id))
            current_lesson.students.add(student)

        return redirect('presence_count:home')
    return render(request, 'lesson/add_lesson.html', {'student_list': student_list, 'lesson_form': lesson_form})


def grades_manager(request):
    student_list = Student.objects.all().order_by('group_id')
    if request.method == 'POST':
        grade1_list = [float(x) for x in request.POST.getlist('grade1')]
        grade2_list = [float(x) for x in request.POST.getlist('grade2')]
        for i in range(len(grade1_list)):
            grade1_list[i] = GRADE_LIMIT if grade1_list[i] > GRADE_LIMIT else grade1_list[i]
            grade1_list[i] = 0.0 if grade1_list[i] < 0.0 else grade1_list[i]

        for i in range(len(grade2_list)):
            grade2_list[i] = GRADE_LIMIT if grade2_list[i] > GRADE_LIMIT else grade2_list[i]
            grade2_list[i] = 0.0 if grade2_list[i] < 0.0 else grade2_list[i]
        
        for i in range(len(student_list)):
            student_list[i].grade_1 = grade1_list[i]
            student_list[i].grade_2 = grade2_list[i]
            student_list[i].grade_avg = (grade1_list[i] + grade2_list[i]) / 2.0
            student_list[i].save()

        return redirect('presence_count:grades_manager')
    return render(request, 'student/update_grades.html', {'student_list': student_list})


def student(request):
    return render(request, 'menus/student_menu.html')


def view_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
    return render(request, 'student/student.html', context)


def edit_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    form = RegisterStudentForm(instance=student)
    context = {'form': form}
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        else:
            print('Error while updating student')
        return redirect('/')
    return render(request, 'student/edit_student.html', context)


def select_student(request):
    students = Student.objects.all().order_by('group_id')
    context = {'students': students}
    return render(request, 'student/student_manager.html', context)
    

def confirm_delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'student/delete_student.html', {'student': student})    


def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/')

def view_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    members = Student.objects.filter(group_id=group_id)
    context = {'group': group, 'members': members}
    return render(request, 'group/group.html', context)


def group(request):
    return render(request, 'menus/group_menu.html')


def select_group(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'group/group_manager.html', context)


def edit_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    form = RegisterGroupForm(instance=group)
    context = {'form': form}
    if request.method == 'POST':
        form = RegisterGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
        else:
            print('Error while editting group')
        return redirect('/')
    return render(request, 'group/edit_group.html', context)


def confirm_delete_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'group/delete_group.html', {'group': group})


def delete_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    Student.objects.filter(group_id=group_id).update(group_id=None)        
    group.delete()
    return redirect('/')


def lesson_manager(request):
    lessons = Lesson.objects.all()
    context = {'lessons': lessons}
    return render(request, 'lesson/lesson_manager.html', context)


def edit_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson_form = RegisterLessonForm(instance=lesson)
    student_list = Student.objects.all().order_by('group_id')
    lesson_students = Lesson.students.through.objects.filter(lesson_id=lesson.id)
    present_students = []
    for ls in lesson_students:
        present_students.append(ls.student_id)

    if request.method == 'POST':
        lesson_data = request.POST.copy()
        if 'boxes' in lesson_data:
            del lesson_data['boxes']
        lesson_form = RegisterLessonForm(lesson_data, instance=lesson) # Change this!
        if lesson_form.is_valid():
            lesson_form.save()
        else:
            print('Error while updating lesson')
        
        for student_id in present_students:
            if str(student_id) not in request.POST.getlist('boxes'):
                print(f'Removing presence from {Student.objects.get(pk=int(student_id))}')
                presence = Lesson.students.through.objects.get(lesson_id=lesson.id, student_id=student_id)
                presence.delete()
                Student.objects.filter(pk=int(student_id)).update(presences=F('presences')-1)
        for student_id in request.POST.getlist('boxes'):
            if not int(student_id) in present_students:
                print(f'Adding presence to {Student.objects.get(pk=int(student_id))}')
                Student.objects.filter(pk=int(student_id)).update(presences=F('presences')+1)
                student = Student.objects.get(pk=int(student_id))
                lesson.students.add(student)
        return redirect('/')
    context = {'lesson_form': lesson_form, 'student_list':student_list, 'present_students':present_students}
    return render(request, 'lesson/edit_lesson.html', context)


def confirm_delete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson_students = Lesson.students.through.objects.filter(lesson_id=lesson.id)
    present_students = []
    for ls in lesson_students:
        present_students.append(ls.student_id)
    students = Student.objects.all()
    context = {'lesson': lesson, 'present_students': present_students, 'students': students}
    return render(request, 'lesson/delete_lesson.html', context)    


def delete_lesson(request, lesson_id):
    lesson_students = Lesson.students.through.objects.filter(lesson_id=lesson_id)
    for ls in lesson_students:
        Student.objects.filter(pk=int(ls.student_id)).update(presences=F('presences')-1)
        ls.delete()
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson.delete()
    return redirect('/')
    
