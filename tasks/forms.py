from django import forms
from django.forms import ModelForm

from .models import Category, Task


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = (
            'topic',
            'description',
            'category',
            'is_regular',
            'due_date'
        )
        help_texts = {
            'topic': 'write a topic',
            'description': 'task description',
            'category': 'write category of task',
            'is_regular': 'if task is regular mark it',
            'due_date': 'specify due date for task'

        }
        widgets = {
            'topic': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'cols': 10,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'cols': 40,
            }),
            'is_regular': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = (
            'name',
        )
        help_texts = {
            'name': 'Specify the name of the category for example "Home"'
        }
        widgets = {
            'name': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'cols': 10,
            }),

        }
