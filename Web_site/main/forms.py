from django.forms import ModelForm, TextInput, Textarea
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "author"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название:'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст:'}),
                   "author": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите автора:'})
                   }