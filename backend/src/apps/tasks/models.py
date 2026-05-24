from django.db import models


class Task(models.Model):
    """
    Model representing a task in the task management system.

    Attributes:
        title (str): The title of the task.
        description (str): A detailed description of the task.
        status (str): The current status of the task (e.g., To Do, In Progress, On Hold, Done).
        due_date (datetime): The date and time by which the task should be completed.
        created_at (datetime): The date and time when the task was created.
        updated_at (datetime): The date and time when the task was last updated.
    """

    class Status(models.TextChoices):
        """Enumeration of possible task statuses."""

        TO_DO = "TO_DO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        ON_HOLD = "ON_HOLD", "On Hold"
        DONE = "DONE", "Done"

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TO_DO,
        blank=False,
        null=False,
    )
    due_date = models.DateTimeField(null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-due_date"]
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return f"{self.title} - {self.status}"
