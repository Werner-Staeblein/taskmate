from django import forms
from todolist_app.models import Task


class TaskListForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'done']
        
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        #     'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        