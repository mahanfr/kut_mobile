from announcement.models import Announcement
from rest_framework.generics import ListAPIView
from announcement.api.serializers import AnnouncementSerializer
from rest_framework import permissions
from announcement.models import Announcement

class AnnounecementsListApi(ListAPIView):
    serializer_class = AnnouncementSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Announcement.objects.all()
        return queryset