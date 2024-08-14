import datetime
from django.db import models


class NoExpiredURLManager(models.Manager):
    """Filter out expired URLs.

    We do not want to delete them, just not show them in the API. That way they can be turned on again in the future.
    """

    def get_queryset(self) -> models.QuerySet:
        queryset = super().get_queryset()
        return queryset.filter(
            models.Q(expires_at__gt=datetime.datetime.now())
            | models.Q(expires_at__isnull=True)
        )


class URL(models.Model):
    # Fields
    original_url: models.URLField = models.URLField()
    short_code: models.CharField = models.CharField(max_length=10, unique=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    expires_at: models.DateTimeField = models.DateTimeField(null=True, blank=True)

    # Managers
    objects = NoExpiredURLManager()
    all_objects: models.Manager = models.Manager()
