from django.urls import path, include
from .views import BoardColumnAPIView, BoardColumnDetailView

urlpatterns = [
    path('boardcolumn/', BoardColumnAPIView.as_view()),
    path('detail/boardcolumn/<int:tableID>/', BoardColumnDetailView.as_view())
]