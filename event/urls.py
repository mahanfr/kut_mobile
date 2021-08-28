from django.urls import path
from event.api.views import EventListApi

urlpatterns = [
    path('', EventListApi.as_view()),
]
