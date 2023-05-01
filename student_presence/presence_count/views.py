from django.shortcuts import redirect, render
from presence_count.forms import RegisterGroupForm, RegisterStudentForm
from .models import Group, Student
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
    return render(request, 'register_student.html', context)



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
    return render(request, 'register_group.html', context)


def roll_call(request):
    student_list = Student.objects.all().order_by('group_id')
    if request.method == 'POST':
        id_list = request.POST.getlist('boxes')
        for student_id in id_list:
            Student.objects.filter(pk=int(student_id)).update(presences=F('presences')+1)

        return redirect('presence_count:home')
    return render(request, 'roll_call.html', {'student_list': student_list})


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
    return render(request, 'update_grades.html', {'student_list': student_list})


def student(request):
    return render(request, 'student_links.html')


def view_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
    return render(request, 'student.html', context)


def view_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    context = {'group': group}
    return render(request, 'group.html', context)
