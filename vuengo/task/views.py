from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets


#API ENDPOINT
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
