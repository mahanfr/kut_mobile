from rest_framework import serializers
from announcement.models import Announcement
from core.utils import TimestampField
from django.utils import timezone

class AnnouncementSerializer(serializers.ModelSerializer):
    timeStamp = serializers.ReadOnlyField(default=timezone.now().timestamp())

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'article_date', 'cover_link','article_link','article','created_at','timeStamp']
