from django.urls import path
from .views import VideoViews

urlpatterns = [
    path("list/", VideoViews.as_view()),
]
