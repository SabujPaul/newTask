from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = "tasks"

urlpatterns = [
    path('', views.home, name='home_page'),
    path('task/', TaskListView.as_view(), name='task_list'),
    path('task/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:task_id>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:task_id>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    
    
]