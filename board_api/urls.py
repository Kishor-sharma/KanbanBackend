from django.urls import path
from .views import BoardAPIView, BoardDetailView

app_name = "board_api"
urlpatterns = [
    path('board/', BoardAPIView.as_view(), name='board'),
    path('detail/board/<int:pk>/', BoardDetailView.as_view(), name='detailview')
]