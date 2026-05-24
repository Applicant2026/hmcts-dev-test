from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from apps.tasks.models import Task


class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            status=Task.Status.TO_DO,
            due_date=timezone.now() + timezone.timedelta(days=1),
        )

    def test_create_task(self):
        payload = {
            "title": "New Task",
            "description": "This is a new task.",
            "status": Task.Status.TO_DO,
            "due_date": timezone.now() + timezone.timedelta(days=2),
        }
        response = self.client.post("/api/v1/tasks/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Task")
        self.assertEqual(response.data["status_display"], "To Do")
        self.assertIn("due_date_display", response.data)

    def test_list_tasks(self):
        response = self.client.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Test Task")

    def test_retrieve_task(self):
        response = self.client.get(f"/api/v1/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Task")
        self.assertEqual(response.data["status_display"], "To Do")
        self.assertIn("due_date_display", response.data)

    def test_update_task_status(self):
        payload = {
            "title": self.task.title,
            "description": self.task.description,
            "status": Task.Status.IN_PROGRESS,
            "due_date": self.task.due_date,
        }
        response = self.client.put(
            f"/api/v1/tasks/{self.task.id}/", payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], Task.Status.IN_PROGRESS)
        self.assertEqual(response.data["status_display"], "In Progress")

    def test_delete_task(self):
        response = self.client.delete(f"/api/v1/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())


class TaskStatusAPIViewTestCase(APITestCase):
    def test_task_statuses_returns_value_label_pairs(self):
        response = self.client.get("/api/v1/task-statuses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertTrue(all("value" in s and "label" in s for s in response.data))
        values = [s["value"] for s in response.data]
        labels = [s["label"] for s in response.data]
        self.assertIn("TO_DO", values)
        self.assertIn("To Do", labels)
