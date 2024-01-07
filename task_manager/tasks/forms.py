from django import forms
from .models import Task, Photo

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        
        fields = ['title', 'description', 'due_date','priority', 'is_complete']
        exclude=['created_at', 'updated_at']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
    