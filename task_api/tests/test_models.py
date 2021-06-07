from django.test import TestCase
from task_api.models import Task

class TestTaskModel(TestCase):
    def setUp(self):
        Task.objects.create(title="Title", description='Description', status=False, columnID=1, boardID=5)
        Task.objects.create(title="Title1", description='Description1', status=True, columnID=1, boardID=4)

    def test_Task_database(self):
        task1 = Task.objects.get(title='Title', description='Description')
        task2 = Task.objects.get(title='Title1', description='Description1')

        self.assertNotEquals(task1.id, task2.id)
        self.assertEquals(task1.__str__(), 'Title')
        self.assertEquals(task2.__str__(), 'Title1')
