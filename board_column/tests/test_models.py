from django.test import TestCase
from board_column.models import BoardColumn

class TestBoardColumnModel(TestCase):
    def setUp(self):
        BoardColumn.objects.create(boardID='1', columnID=1, limit=5, capacity=20)
        BoardColumn.objects.create(boardID='1', columnID=2, limit=5, capacity=20)

    def test_data_in_database(self):
        data1 = BoardColumn.objects.get(boardID='1', columnID=1)
        data2 = BoardColumn.objects.get(boardID='1', columnID=2)

        self.assertEquals(data1.id, 1)
        self.assertEquals(data2.id, 2)