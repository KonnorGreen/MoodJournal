from django.db import models

# Create your models here.

class Journal(models.Model):
    date = models.DateField((""), auto_now=False, auto_now_add=False)
    time = models.TimeField((""), auto_now=False, auto_now_add=False)
    mood = models.CharField((""), max_length=20)
    entry = models.TextField((""))

    def __str__(self):
        return f"{self.date} to {self.mood}"
