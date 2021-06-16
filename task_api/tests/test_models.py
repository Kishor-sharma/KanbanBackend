from django.contrib.auth.models import User
from board_api.models import Board
from column_api.models import Lanes
from django.test import TestCase
from task_api.models import Task

class TestTaskModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="myth", email="kishorkmr2002@gmail.com", password="top_secret")
        column1 = Lanes.objects.create(name="TODO", index=1)
        board1 = Board.objects.create(name="Cleaning", user=self.user)
        board2 = Board.objects.create(name="Gardening", user=self.user)
        Task.objects.create(title="Title", description='Description', status=False, column=column1, board=board1)
        Task.objects.create(title="Title1", description='Description1', status=True, column=column1, board=board2)

    def test_Task_database(self):
        task1 = Task.objects.get(title='Title', description='Description')
        task2 = Task.objects.get(title='Title1', description='Description1')

        self.assertNotEquals(task1.id, task2.id)
        self.assertEquals(task1.__str__(), 'Title')
        self.assertEquals(task2.__str__(), 'Title1')
