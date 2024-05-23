from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_name_en = models.CharField(max_length=100,default='')
    event_cover = models.ImageField(upload_to='events/')
    date = models.DateField()
    details = models.TextField()
    details_en = models.TextField(default='')

    def __str__(self):
        return self.event_name


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_images')
    image = models.ImageField(upload_to='events/images/')

    def __str__(self):
        return f"Image for {self.event.event_name}"


class Service(models.Model):
    TITLE_CHOICES = [
        ('consultation', 'consultation'),
        ('physio_therapy', 'physio_therapy'),
        ('MEDEINE GENERALCE', 'MEDECINE GENERALE'),
        ('IMAGERIE MEDICALE', 'IMAGERIE MEDICALE'),
        ('REHABILITATION FONCTIONNELLE', 'REHABILITATION FONCTIONNELLE'),
    ]

    title = models.CharField(choices=TITLE_CHOICES, max_length=100, unique=True)
    detail = HTMLField()
    detail_en = HTMLField(default='')

    def __str__(self):
        return self.title