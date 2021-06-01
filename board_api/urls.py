from django.urls import path
from .views import BoardAPIView, BoardDetailView

urlpatterns = [
    path('board/', BoardAPIView.as_view()),
    path('detail/board/<int:pk>/', BoardDetailView.as_view())
]