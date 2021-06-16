from django.urls import path, include
from .views import BoardColumnAPIView, BoardColumnDetailView

urlpatterns = [
    path('boardcolumn/', BoardColumnAPIView.as_view(), name='boardcolumnlist'),
    path('detail/boardcolumn/<int:table_id>/', BoardColumnDetailView.as_view(), name='detailboardcolumn')
]