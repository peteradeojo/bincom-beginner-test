from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

from .models import Task
from .forms import TaskForm


# Create your views here.
def index(r):
    tasks = Task.objects.all().order_by('status', '-date_added')

    form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(r, 'tasks/index.html', context)


def new_task(r):
    if r.method != 'POST':
      return HttpResponseBadRequest()
    
    form = TaskForm(data=r.POST)
    if form.is_valid():
      form.save()

    return redirect('tasks:index')


def toggle(r, task_id):
    task = Task.objects.get(id=task_id)

    task.status = not task.status
    task.save()
    return redirect('tasks:index')


def delete(r, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    # pass
    return redirect('tasks:index')
