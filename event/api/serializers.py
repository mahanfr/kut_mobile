from rest_framework import serializers
from event.models import Event
from core.utils import TimestampField
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    # timeStamp = serializers.ReadOnlyField(default=timezone.now().timestamp())

    class Meta:
        model = Event
        fields = ['subject','start_date','end_date','start_time','end_time','priority']
