from django.urls import path
from announcement.api.views import AnnounecementsListApi

urlpatterns = [
    path('', AnnounecementsListApi.as_view()),
]
