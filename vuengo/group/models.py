from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model): 
    description = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='user_taskG', on_delete=models.CASCADE)
    

