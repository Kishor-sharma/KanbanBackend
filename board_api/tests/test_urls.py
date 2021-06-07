from django.test import TestCase
from django.urls import reverse, resolve
from board_api.views import BoardAPIView, BoardDetailView

class TestUrls(TestCase):
    def test_list_url_resolve(self):
        url = reverse('board_api:board')
        self.assertEquals(resolve(url).func.view_class, BoardAPIView)

    def test_detail_view_resolve(self):
        url = reverse('board_api:detailview', args=[1])
        self.assertEquals(resolve(url).func.view_class, BoardDetailView)