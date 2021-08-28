from django.urls import path
from news.api.views import NewsListApi

urlpatterns = [
    path('', NewsListApi.as_view()),
]
