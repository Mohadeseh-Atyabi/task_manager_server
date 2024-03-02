from django.shortcuts import render, redirect
from .task import Task
from .models import TaskModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


@login_required
def create_task(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form = Task(req.POST)
            if form.is_valid():
                task = TaskModel(
                    title=form.cleaned_data.get('title'),
                    description=form.cleaned_data.get('description'),
                    duration=form.cleaned_data.get('duration'),
                    start_date=form.cleaned_data.get('start_date'),
                    owner=req.user
                )
                task.save()
                return redirect('show task')
        else:
            form = Task()
        return render(req, 'create_task.html', {'form': form})
    else:
        return redirect('/login/')


@login_required
def show_task(req):
    tasks = TaskModel.objects.filter(owner=req.user)
    return render(req, 'show_task.html', {'tasks': tasks})


@login_required
def edit_task(req, id):
    task = TaskModel.objects.get(id=id)
    if req.method == 'POST':
        form = Task(req.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.duration = form.cleaned_data.get('duration')
            task.start_date = form.cleaned_data.get('start_date')
            task.save()
            return redirect('show_task')
    else:

        form = Task(initial={'title': task.title, 'description': task.description,
                             'duration': task.duration, 'start_date': task.start_date})

    return render(req, 'edit_task.html', {'form': form})
