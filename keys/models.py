from django.db import models
from django.forms import CharField


class Key(models.Model):
    A = "A"
    BFLAT = "B-flat/A#"
    B = "B"
    C = "C"
    CSHARP = "C#/D-flat"
    D = "D"
    EFLAT = "E-flat/D#"
    E = "E"
    F = "F"
    FSHARP = "F#"
    G = "G"
    GSHARP = "A-flat/G#"
    KEY_NAME_CHOICES = [
        (A, "A"),
        (BFLAT, "B-flat/A#"),
        (B, "B"),
        (C, "C"),
        (CSHARP, "C#/D-flat"),
        (D, "D"),
        (EFLAT, "E-flat/D#"),
        (E, "E"),
        (F, "F"),
        (FSHARP, "F#"),
        (G, "G"),
        (GSHARP, "A-flat/G#"),
    ]

    name = models.CharField(max_length=20, choices=KEY_NAME_CHOICES, default=A)
    date = models.DateField()
    tempo = models.CharField(max_length=200, default="None specified")
    notes = models.TextField()
    assignee = models.ForeignKey(
        "auth.User", related_name="keys", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
