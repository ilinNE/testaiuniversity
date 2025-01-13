from rest_framework import mixins, viewsets

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
