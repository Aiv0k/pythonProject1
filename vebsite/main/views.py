from django.shortcuts import render, redirect
from .models import Task

from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'title': 'Главная страница', "tasks": tasks})


def information(request):
    return render(request, "information.html")


def about(request):
    return render(request, "about.html")


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)