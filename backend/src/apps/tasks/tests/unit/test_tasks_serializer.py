import datetime
from unittest import TestCase
from django.utils import timezone
from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class TaskSerializerTestCase(TestCase):
    def test_serializer_accepts_valid_future_date(self):
        future_date = timezone.now() + timezone.timedelta(days=2)
        payload = {
            "title": "Test Task",
            "description": "This is a test task.",
            "status": Task.Status.TO_DO,
            "due_date": future_date,
        }
        serializer = TaskSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], "Test Task")

    def test_serializer_rejects_past_date(self):
        past_date = timezone.now() - timezone.timedelta(days=2)
        payload = {
            "title": "Test Task",
            "description": "This is a test task.",
            "status": Task.Status.TO_DO,
            "due_date": past_date,
        }
        serializer = TaskSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn("due_date", serializer.errors)
        self.assertEqual(
            serializer.errors["due_date"][0], "Due date cannot be in the past."
        )

    def test_serializer_rejects_invalid_status(self):
        future_date = timezone.now() + timezone.timedelta(days=2)
        payload = {
            "title": "Test Task",
            "status": "INVALID_STATUS",
            "due_date": future_date,
        }
        serializer = TaskSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn("status", serializer.errors)

    def test_status_display_returns_human_readable_label(self):
        task = Task(
            title="Test Task",
            status=Task.Status.IN_PROGRESS,
            due_date=timezone.now() + timezone.timedelta(days=1),
        )
        serializer = TaskSerializer(instance=task)
        self.assertEqual(serializer.data["status_display"], "In Progress")

    def test_due_date_display_returns_formatted_string(self):
        due_date = datetime.datetime(2026, 5, 31, 10, 30, tzinfo=datetime.timezone.utc)
        task = Task(
            title="Test Task",
            status=Task.Status.TO_DO,
            due_date=due_date,
        )
        serializer = TaskSerializer(instance=task)
        self.assertIn("31", serializer.data["due_date_display"])
        self.assertIn("May", serializer.data["due_date_display"])
        self.assertIn("2026", serializer.data["due_date_display"])
        self.assertIn("10:30", serializer.data["due_date_display"])
