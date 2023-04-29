from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)