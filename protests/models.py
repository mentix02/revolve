from datetime import datetime
from typing import List

from django.db import models


class Protest(models.Model):

    venue_lat: int = models.BigIntegerField()
    venue_long: int = models.BigIntegerField()
    name: str = models.CharField(max_length=250)
    slug: str = models.SlugField(max_length=200)
    description: str = models.TextField(help_text='Details about the protest.')
    datetime: datetime = models.DateTimeField(help_text='Date and time for protest.')
    organizer = models.ForeignKey(
        'user.User', null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        indexes: List[models.Index] = [
            models.Index(fields=('slug',)),
        ]
