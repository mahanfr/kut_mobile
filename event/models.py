from django.db import models
from django.db.models.fields import TimeField

class Event(models.Model):
    priority_list = [
        (0,'normal'),
        (1,'important'),
    ]
    subject = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    start_time =  models.TimeField(blank=True,null=True)
    end_time =  models.TimeField(blank=True,null=True)
    priority = models.PositiveSmallIntegerField(default=0,choices=priority_list)

    def __str__(self) -> str:
        return self.subject