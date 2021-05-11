from django.db import models
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
  details = models.TextField(max_length=250)

  def __str__(self):
    return self.details

  def get_absolute_url(self):
      return reverse("home")
  