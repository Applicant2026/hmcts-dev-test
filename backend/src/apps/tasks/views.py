from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """API endpoint that allows CRUD operations on tasks."""

    queryset = Task.objects.all().order_by("due_date")
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["due_date", "created_at", "status"]
    ordering = ["due_date"]
    search_fields = ["title", "description"]


class TaskStatusAPIView(viewsets.ViewSet):
    """API endpoint to retrieve distinct task statuses."""

    permission_classes = [AllowAny]

    def list(self, request):
        statuses = [{"value": value, "label": label} for value, label in Task.Status.choices]
        return Response(statuses)
