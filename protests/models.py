from typing import List
from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Protest(models.Model):

    slug: str = models.SlugField(max_length=200)
    venue_lat: int = models.FloatField(help_text='Venue latitude.')
    venue_long: float = models.FloatField(help_text='Venue longitude.')
    description: str = models.TextField(help_text='Details about the protest.')
    datetime: datetime = models.DateTimeField(help_text='Date and time for protest.')
    name: str = models.CharField(
        max_length=250, help_text='Name of organisation or event.'
    )
    organizer = models.ForeignKey(
        'user.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='organized_protests',
    )

    def get_absolute_url(self):
        return reverse('protests:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs) -> None:
        self.slug = f'{slugify(self.name)}'
        super().save(*args, **kwargs)

    class Meta:
        indexes: List[models.Index] = [
            models.Index(fields=('slug',)),
        ]
