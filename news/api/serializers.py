from rest_framework import serializers
from news.models import News
from core.utils import TimestampField
from django.utils import timezone

class NewsSerializer(serializers.ModelSerializer):
    # timeStamp = serializers.ReadOnlyField(default=timezone.now().timestamp())

    class Meta:
        model = News
        fields = ['id', 'title', 'article_date', 'cover_link','article_link','article','created_at']
