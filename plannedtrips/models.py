from django.db import models

class PlannedTrip(models.Model):
  user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
  gpt_response = models.JSONField(null=True, blank=True)
