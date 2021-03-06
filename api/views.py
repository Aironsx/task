from rest_framework import permissions, viewsets

from tasks.models import Category, Task

from .permissions import IsOwnerUpdate
from .serializer import CategorySerializer, TaskSerializer


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerUpdate, permissions.IsAuthenticated)

    def get_queryset(self):
        if self.request.query_params.get('delayed_task'):
            return Task.objects.filter(
                author=self.request.user,
                delayed_task=True
            )
        if self.request.query_params.get('coming_soon_task'):
            return Task.objects.filter(
                author=self.request.user,
                coming_soon_task=True
            )
        return Task.objects.filter(author=self.request.user, is_done=False)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerUpdate, permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Category.objects.filter(author=self.request.user)
