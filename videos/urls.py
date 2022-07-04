from django.urls import path
from .views import VideoViews, SingleVideos

urlpatterns = [
    path("list/", VideoViews.as_view()),
    path("list/<int:id>/", SingleVideos.as_view()),
]
