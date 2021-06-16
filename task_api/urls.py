from django.urls import path
from .views import TaskAPIView, TaskDetailView

urlpatterns = [
    path('task/', TaskAPIView.as_view(), name='tasklist'),
    path('task/<int:board_id>/', TaskAPIView.as_view(), name='taskwithboard'),
    path('task/<int:board_id>/<int:column_id>/', TaskAPIView.as_view(), name='taskwithboardcolumn'),
    path('detail/task/<int:pk>/', TaskDetailView.as_view(), name='detailtask'),
]