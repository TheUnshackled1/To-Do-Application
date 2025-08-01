from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks.html', context)
def edit_Task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'edit_Task.html', context)

def delete_Task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    context = {'task':task}
    return render(request, 'delete_Task.html', context)