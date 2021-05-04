from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=30,null=True)
    desc = models.CharField(max_length=30,null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task