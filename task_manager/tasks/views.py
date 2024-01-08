
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task, Photo
from .serializers import TaskSerializer, PhotoSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from .forms import TaskForm, PhotoForm


def home(request):
    return render(request, "base.html") 

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks:login')
    template_name = 'signup.html'

class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    next_page = 'tasks:home_page'

class LogoutUserView(LogoutView):
    next_page = 'tasks:login'

class TaskListView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        tasks = Task.objects.filter(title__icontains=search_query).order_by('is_complete','-priority', 'due_date')
        return render(request, 'task_list.html', {'tasks': tasks})

class TaskDetailView(View):

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        photos = task.photos.all()
        photo_form = PhotoForm()
        return render(request, 'task_detail.html', {'task': task, 'photos': photos, 'photo_form': photo_form})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        photos = task.photos.all()
        
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            new_photo = photo_form.save(commit=False)
            new_photo.task = task
            new_photo.save()
            return redirect('tasks:task_detail', task_id=task.id)

        return render(request, 'task_detail.html', {'task': task, 'photos': photos, 'photo_form': photo_form})

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
        form = TaskForm(request.POST, request.FILES,instance=task)
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
    
class PhotoDeleteView(View):
    def get(self,request,photo_id):
       
        photo = get_object_or_404(Photo, id=photo_id)
        return render(request, 'delete_photo.html', { 'photo': photo})

    def post(self,request,photo_id):
        
        photo = get_object_or_404(Photo, id=photo_id)
        
        if request.method == 'POST':
            photo.delete()
            return redirect(reverse('tasks:task_list'))


# Api view

class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class PhotoListAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated] 
