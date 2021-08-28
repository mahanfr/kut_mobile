from rest_framework import serializers
from django.utils import timezone

class TimestampField(serializers.Field):
    def to_representation(self):
        return timezone.now.timestamp()*1000