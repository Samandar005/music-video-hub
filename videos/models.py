from django.db import models
from django.shortcuts import reverse

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateField()
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('videos:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('videos:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('videos:delete', args=[self.pk])