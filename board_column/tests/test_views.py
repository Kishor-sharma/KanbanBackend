from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls.base import resolve
from board_column.views import BoardColumnAPIView, BoardColumnDetailView
from board_api.models import Board
from column_api.models import Lanes
from board_column.models import BoardColumn

# Create your tests here.
class TestBoardColumnView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adam', email='adam@mail.com', password='top_secret')
        self.validClient = Client()
        self.validClient.login(username='adam', password='top_secret')
        self.url = reverse('boardcolumnlist')
        self.detailUrl = reverse('detailboardcolumn', args=[1])
        self.wrongdetailUrl = reverse('detailboardcolumn', args=[6])
        Board.objects.create(name='Board', userID=self.user.id)
        Lanes.objects.create(name='TODO', index=2)
        self.data = {
            "boardID": 1,
            "columnID": 1,
            "capacity": 10,
            "limit": 5
        }
        BoardColumn.objects.create(boardID = 1, columnID = 1, capacity = 10, limit = 5)

    def test_authorization_fail(self):
        response = Client().get(self.url)
        self.assertEquals(response.status_code, 401)

    def test_GET_all_data(self):
        response = self.validClient.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_POST_data(self):
        response = self.validClient.post(self.url, self.data, content_type='application/json')
        self.assertEquals(response.status_code, 201)

        alterd_data = self.data
        alterd_data['columnID'] = 20
        response = self.validClient.post(self.url, alterd_data, content_type='application/json')
        self.assertEquals(response.status_code, 406)

        alterd_data['columnID'] = 1
        alterd_data['boardID'] = 13
        response = self.validClient.post(self.url, alterd_data, content_type='application/json')
        self.assertEquals(response.status_code, 406)

        del alterd_data['columnID']
        del alterd_data['boardID']
        alterd_data['random'] = 2
        response = self.validClient.post(self.url, alterd_data, content_type='application/json')
        self.assertEquals(response.status_code, 403)

    def test_detail_GET_data(self):
        response = self.validClient.get(self.detailUrl)
        self.assertEquals(response.status_code, 200)
        response = self.validClient.get(self.wrongdetailUrl)
        self.assertEquals(response.status_code, 404)