from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
  username = models.CharField(max_length=70, unique=True)
  first_name = models.CharField(max_length=70, blank=True)
  last_name = models.CharField(max_length=70, blank=True)
  email = models.EmailField(unique=True)
  uuid = models.UUIDField(blank=True, null=True)

  def save(self, *args, **kwargs):
    self.uuid = uuid.uuid4()
    return super().save(*args, **kwargs)