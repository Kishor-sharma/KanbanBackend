from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve

class TestColumnAPIView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="dummy", email="dummy@mail.com", password="top_secret")
        self.validClient = Client()
        self.validClient.login(username="dummy", password="top_secret")
        self.url = reverse('column')
        self.detailurl = reverse('detailcolumn', args=[1])
        self.wrongURL = reverse('detailcolumn', args=[19])
        self.data = {"name": "UNCATEGORY", "index": 0}

    def test_authorization_fail(self):
        unauthorizedCLient = Client()
        response = unauthorizedCLient.get(self.url)
        self.assertEquals(response.status_code, 401)

    def test_GET_list(self):
        response = self.validClient.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_POST_data(self):
        response = self.validClient.post(self.url, self.data, content_type='application/json')
        self.assertEquals(response.status_code, 201)

    def test_POST_invalid_data(self):
        response = self.validClient.post(self.url, {'anything': 'anythong', 'jpt': 'jtp'}, content_type='application/json')
        self.assertEquals(response.status_code, 400)

    def test_detail_GET_data(self):
        self.test_POST_data()
        response = self.validClient.get(self.detailurl)
        self.assertEquals(response.status_code, 200)
        response = self.validClient.get(self.wrongURL)
        self.assertEquals(response.status_code, 404)

    def test_detail_PUT_date(self):
        self.test_POST_data()
        response = self.validClient.put(self.detailurl, {"name": "updated UNCATEGORY", "index": 1}, content_type='application/json')
        self.assertEquals(response.status_code, 200)
        response = self.validClient.put(self.wrongURL, {"name": "updated UNCATEGORY", "index": 1}, content_type='application/json')
        self.assertEquals(response.status_code, 404)

    def test_detail_DELETE_data(self):
        self.test_POST_data()
        response = self.validClient.delete(self.detailurl)
        self.assertEquals(response.status_code, 204)
        response = self.validClient.delete(self.wrongURL)
        self.assertEquals(response.status_code, 404)