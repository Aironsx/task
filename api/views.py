from django.shortcuts import render
from rest_framework import viewsets

from serializer import TaskSerializer
from tasks.models import Task


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


