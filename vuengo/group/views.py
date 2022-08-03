from django import views
from django.shortcuts import render
from rest_framework import viewsets

from .models import Group
from .serializers import GroupSerializer

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by= self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)