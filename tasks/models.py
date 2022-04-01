from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project", related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        "auth.User",
        related_name="tasks",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
