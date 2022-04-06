from django.db import models
from django.forms import CharField


class Key(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    tempo = models.CharField(max_length=200, default="None specified")
    notes = models.TextField()
    assignee = models.ForeignKey(
        "auth.User", related_name="keys", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
