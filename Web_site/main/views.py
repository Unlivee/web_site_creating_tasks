from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def index(request):
    task = Task.objects.order_by('id')

    context = {
        'tasks': task,

    }
    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "форма была не верной"
            return error

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context=context)

def detels(request, pk):
    task = Task.objects.get(pk=pk)

    context = {
        "task": task
    }

    return render(request, "main/detels.html", context=context)

def delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {
        "task": task
    }

    return render(request, "main/delete.html", context=context)

