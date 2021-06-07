from django.urls import path
from .views import TaskAPIView, TaskDetailView

urlpatterns = [
    path('task/', TaskAPIView.as_view(), name='tasklist'),
    path('task/<int:boardID>/', TaskAPIView.as_view(), name='taskwithboard'),
    path('task/<int:boardID>/<int:columnID>/', TaskAPIView.as_view(), name='taskwithboardcolumn'),
    path('detail/task/<int:pk>/', TaskDetailView.as_view(), name='detailtask'),
]