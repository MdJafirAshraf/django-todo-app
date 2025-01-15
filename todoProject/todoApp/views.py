from django.shortcuts import redirect, get_object_or_404
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