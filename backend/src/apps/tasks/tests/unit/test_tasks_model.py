from django.test import TestCase
from django.utils import timezone
from apps.tasks.models import Task


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            status=Task.Status.TO_DO,
            due_date=timezone.now() + timezone.timedelta(days=1),
        )

    def test_task_creation_happy_path(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")
        self.assertEqual(self.task.status, Task.Status.TO_DO)
        self.assertTrue(self.task.due_date > timezone.now())
        self.assertTrue(self.task.created_at is not None)
        self.assertTrue(self.task.updated_at is not None)

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), "Test Task - TO_DO")

    def test_task_creation_without_description(self):
        self.task = Task.objects.create(
            title="Test Task",
            description=None,
            status=Task.Status.TO_DO,
            due_date=timezone.now() + timezone.timedelta(days=1),
        )

        self.assertEqual(self.task.title, "Test Task")
        self.assertIsNone(self.task.description)
        self.assertEqual(self.task.status, Task.Status.TO_DO)
        self.assertTrue(self.task.due_date > timezone.now())
        self.assertTrue(self.task.created_at is not None)
        self.assertTrue(self.task.updated_at is not None)

    def test_default_status_fallback(self):
        self.task = Task.objects.create(
            title="Test Task",
            due_date=timezone.now() + timezone.timedelta(days=1),
        )

        self.assertEqual(self.task.status, Task.Status.TO_DO)
