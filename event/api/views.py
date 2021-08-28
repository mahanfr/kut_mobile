from rest_framework.generics import ListAPIView
from event.api.serializers import EventSerializer
from rest_framework import permissions
from event.models import Event

class EventListApi(ListAPIView):
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset