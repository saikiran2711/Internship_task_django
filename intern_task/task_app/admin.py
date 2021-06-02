from django.contrib import admin
from .models import TaskUpload

class TaskUploadAdmin(admin.ModelAdmin):
    fields = [
        'task_title',
        'task_description',
        'task_pic',
        'create_timestamp',
    ]

    readonly_fields = ['create_timestamp', ]

    class Meta:
        model = TaskUpload


admin.site.register(TaskUpload,TaskUploadAdmin)
