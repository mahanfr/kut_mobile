from rest_framework.generics import ListAPIView
from announcement.api.serializers import AnnouncementSerializer
from rest_framework import permissions
from news.models import News

class NewsListApi(ListAPIView):
    serializer_class = AnnouncementSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = News.objects.all()
        return queryset