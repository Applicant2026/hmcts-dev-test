from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model with custom validation for due_date."""

    status_display = serializers.SerializerMethodField()
    due_date_display = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "status_display", "due_date", "due_date_display", "created_at", "updated_at"]
        read_only_fields = ["id", "status_display", "due_date_display", "created_at", "updated_at"]

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_due_date_display(self, obj):
        return obj.due_date.strftime("%-d %B %Y at %H:%M")

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