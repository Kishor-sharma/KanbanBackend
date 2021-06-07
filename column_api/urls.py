from django.urls import path
from .views import LaneAPIView, LaneDetailView

urlpatterns = [
    path('column/', LaneAPIView.as_view(), name='column'),
    path('detail/column/<int:pk>/', LaneDetailView.as_view(), name='detailcolumn')
]