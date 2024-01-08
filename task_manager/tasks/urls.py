from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, PhotoDeleteView, SignUpView, LoginUserView, LogoutUserView,  TaskListAPIView, TaskDetailAPIView,PhotoListAPIView, PhotoDetailAPIView

app_name = "tasks"

urlpatterns = [
    path('', views.home, name='home_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('task/', TaskListView.as_view(), name='task_list'),
    path('task/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:task_id>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:task_id>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/delete/<int:photo_id>/', PhotoDeleteView.as_view(), name='photo_delete'),
    


    path('api/tasks/', TaskListAPIView.as_view(), name='api_task_list'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='api_task_detail'),
    path('api/photos/', PhotoListAPIView.as_view(), name='api_photo_list'),
    path('api/photos/<int:pk>/', PhotoDetailAPIView.as_view(), name='api_photo_detail'),
    
]