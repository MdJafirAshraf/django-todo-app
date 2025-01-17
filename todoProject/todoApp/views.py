from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todoApp.models import Task

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def markAsDone(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = True
    task.save()
    return redirect('home')


def setAsIncomplete(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()
    return redirect('home')


def editTask(request, id):
    getTask = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        getTask.task = request.POST['task']
        getTask.save()

        return redirect('home')
    
    else:
        context = {
            'task': getTask
        }

    return render(request, 'edit.html', context)
    

def deleteTask(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')
