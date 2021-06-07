from django.test import TestCase
from django.urls import reverse, resolve
from column_api.views import LaneAPIView, LaneDetailView

# Create your tests here.
class TestUrls(TestCase):
    def test_URL_column_list(self):
        url = reverse('column')
        self.assertEquals(resolve(url).func.view_class, LaneAPIView)

    def test_URL_column_detail(self):
        url = reverse('detailcolumn', args=[1])
        self.assertEquals(resolve(url).func.view_class, LaneDetailView)