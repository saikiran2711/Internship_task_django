from django.db import models

# Create your models here.



class Heirarchy(models.Model):
    sid = models.IntegerField()
    title = models.TextField(max_length=40)
    parentId = models.IntegerField(null= True, default=None, blank=True)

    def __str__(self):
        return f"{self.title}"