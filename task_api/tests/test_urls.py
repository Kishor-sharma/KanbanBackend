from django.conf.urls import url
from django.test import TestCase
from django.urls import resolve, reverse
from task_api.views import TaskAPIView, TaskDetailView

class TestTaskUrls(TestCase):
    def test_task_list_url(self):
        url = reverse('tasklist')
        self.assertEquals(resolve(url).func.view_class, TaskAPIView)

    def test_task_list_of_one_board(self):
        url = reverse('taskwithboard', args=[1])
        self.assertEquals(resolve(url).func.view_class, TaskAPIView)

    def test_task_list_of_one_board_one_column(self):
        url = reverse('taskwithboardcolumn', args=[1,2])
        self.assertEquals(resolve(url).func.view_class, TaskAPIView)

    def test_detail_task_url(self):
        url = reverse('detailtask', args=[1])
        self.assertEquals(resolve(url).func.view_class, TaskDetailView)