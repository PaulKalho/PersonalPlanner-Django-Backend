from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import User
from group.models import Group
import datetime
# Create your models here.

class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = {
        (TODO, 'Todo'),
        (DONE, 'Done'),
    }

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
    date = models.DateField(null=True, blank = True)
    group = models.ForeignKey(Group, related_name='group_desc', on_delete=models.CASCADE, null=True, blank = True )
    created_by = models.ForeignKey(User, related_name='user_task', on_delete=models.CASCADE, default=1)