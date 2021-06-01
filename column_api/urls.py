from django.urls import path
from .views import LaneAPIView, LaneDetailView

urlpatterns = [
    path('column/', LaneAPIView.as_view()),
    path('detail/column/<int:pk>/', LaneDetailView.as_view())
]