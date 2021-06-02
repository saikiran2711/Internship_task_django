
from .models import TaskUpload
from django import forms


class TaskUploadForm(forms.ModelForm):
    class Meta:
        model = TaskUpload
        fields = ('task_title', 'task_description','task_pic',)