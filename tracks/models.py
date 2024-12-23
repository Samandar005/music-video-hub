from django.db import models
from django.shortcuts import reverse


class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='cover_images/')
    audio_file = models.FileField(upload_to='audio_files/')

    def get_detail_url(self):
        return reverse('tracks:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('tracks:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('tracks:delete', args=[self.pk])