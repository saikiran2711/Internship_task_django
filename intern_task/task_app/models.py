from django.db import models
from django.contrib.auth.models import User


class TaskUpload(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.TextField(max_length=200)
    task_description = models.TextField(max_length=2000, blank=True, null= True)
    task_pic = models.ImageField( upload_to='images',blank= True)
    create_timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.uid.username}'s Upload"

    class Meta:
        ordering = ["-create_timestamp"]


