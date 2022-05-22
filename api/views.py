from rest_framework import viewsets, permissions

from .serializer import TaskSerializer
from tasks.models import Task
from .permissions import IsOwnerUpdate


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsOwnerUpdate, permissions.IsAuthenticated)

    def get_queryset(self):
        return Task.objects.filter(is_done=True)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


