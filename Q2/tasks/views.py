from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm


# Create your views here.
@login_required
def index(r):
    tasks = Task.objects.filter(owner_id=r.user.id).order_by('status', '-date_added')

    form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(r, 'tasks/index.html', context)

@login_required
def new_task(r):
    if r.method != 'POST':
      return HttpResponseBadRequest()
    
    form = TaskForm(data=r.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.owner = r.user
      task.save()
    return redirect('tasks:index')

@login_required
def toggle(r, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner == r.user:
      task.status = not task.status
      task.save()
    return redirect('tasks:index')

@login_required
def delete(r, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner.id == r.user.id:
      # task.status = not task.status
      # task.save()
      task.delete()
    # pass
    return redirect('tasks:index')
