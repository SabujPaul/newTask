
from .models import Task
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from .forms import TaskForm 


def home(request):
    #task = Task.objects.all()

    return render(request, "base.html") 

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})

class TaskDetailView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, 'task_detail.html', {'task': task})

class TaskCreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  
            task.save()
            return redirect(reverse('tasks:task_list'))
        return render(request, 'task_create.html', {'form': form})

class TaskUpdateView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_update.html', {'form': form, 'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:task_list'))
        return render(request, 'task_update.html', {'form': form, 'task': task})

class TaskDeleteView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect(reverse('tasks:task_list'))
