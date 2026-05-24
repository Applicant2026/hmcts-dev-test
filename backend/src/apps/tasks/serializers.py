from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model with custom validation for due_date."""

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "due_date", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_status(self, value):
        if value not in Task.Status.values:
            raise serializers.ValidationError(
                f"Invalid status. Must be one of: {', '.join(Task.Status.values)}"
            )
        return value

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value