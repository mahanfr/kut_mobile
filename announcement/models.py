from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    article_date = models.DateField(default=timezone.now)
    cover_link = models.URLField(max_length=510)
    article_link = models.URLField(max_length=510)
    article = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.created_at}'