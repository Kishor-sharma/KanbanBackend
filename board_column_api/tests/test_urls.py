from django.test import TestCase
from django.urls import reverse, resolve
from board_column_api.views import BoardColumnAPIView, BoardColumnDetailView

class TestBoardColumnUrl(TestCase):
    def test_list_url(self):
        url = reverse('boardcolumnlist')
        self.assertEquals(resolve(url).func.view_class, BoardColumnAPIView)

    def test_detail_url(self):
        url = reverse('detailboardcolumn', args=[1])
        self.assertEquals(resolve(url).func.view_class, BoardColumnDetailView)
