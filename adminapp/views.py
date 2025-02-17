from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from . import services
from .forms import FacultyForm, KafedraForm, SubjectForm, TeacherForm, GroupForm, StudentForm
from .models import Faculty, Kafedra, Subject, Teacher, Group, Student


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)

        if user is not None:
            login(request, user)
            return redirect('home_page')

    return render(request, 'login.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = 'signup.html'


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    kafedras = services.get_kafedras()
    subjects = services.get_subjects()
    teachers = services.get_teachers()
    groups = services.get_groups()
    students = services.get_students()

    ctx = {
        "counts": {
            "faculties": len(faculties),
            "kafedras": len(kafedras),
            "subjects": len(subjects),
            "teachers": len(teachers),
            "groups": len(groups),
            "students": len(students)
        }
    }
    return render(request, 'index.html', ctx)


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, "faculty/list.html", ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("faculty_list")

    ctx = {
        "form": form
    }

    return render(request, "faculty/form.html", ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("faculty_list")
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "faculty/form.html", ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedras()
    print(kafedras)
    ctx = {
        'kafedras': kafedras
    }
    return render(request, 'kafedra/list.html', ctx)


@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("kafedra_list")
    ctx = {
        "model": model,
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subjects()
    print(subjects)
    ctx = {
        'subjects': subjects
    }
    return render(request, "subject/list.html", ctx)


@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("subject_list")
    ctx = {
        "form": form
    }
    return render(request, "subject/form.html", ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("subject_list")
    ctx = {
        "model": model,
        'form': form
    }
    return render(request, "subject/form.html", ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def teacher_list(request):
    teachers = Teacher.objects.select_related('subject', 'kafedra').all()
    print(teachers)
    ctx = {
        'teachers': teachers
    }
    return render(request, 'teacher/list.html', ctx)


@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST, instance=model)

    if request.method == "POST" and form.is_valid():
        teacher = form.save(commit=False)
        teacher.subject = form.cleaned_data['subject']
        teacher.kafedra = form.cleaned_data['kafedra']
        teacher.save()
        return redirect('teacher_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, "teacher/form.html", ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return redirect("teacher_list")


@login_required_decorator
def group_list(request):
    groups = Group.objects.select_related('faculty').all()
    print(groups)
    ctx = {
        "groups": groups
    }
    return render(request, "group/list.html", ctx)


@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("group_list")
    ctx = {
        "form": form
    }
    return render(request, "group/form.html", ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("group_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "group/form.html", ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    model.delete()
    return redirect("group_list")


@login_required_decorator
def student_list(request):
    students = Student.objects.select_related('group').all()
    print(students)
    ctx = {
        "students": students
    }
    return render(request, "student/list.html", ctx)


@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        'form': form
    }
    return render(request, "student/form.html", ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "student/form.html", ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')
