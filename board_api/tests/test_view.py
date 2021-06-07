from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class TestBoardAPIView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Kishor', email='admin@admin.com', password='top_secret')
        self.validClient = Client()
        self.validClient.login(username="Kishor", password="top_secret")
        self.url = reverse('board_api:board')
        self.detailUrl = reverse('board_api:detailview', args=[1])
        self.wrongUrl = reverse('board_api:detailview', args=[10])

    def test_authorization_failed(self):
        client = Client()
        response = client.get(self.url)
        self.assertEquals(response.status_code, 401)

    def test_authorization_success(self):        
        response = self.validClient.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_POST_data(self):
        response = self.validClient.post('/board/' , {'name': 'TestBoard'})
        self.assertEquals(response.status_code, 201)
        response = self.validClient.post('/board/', {'naem': 'TestBoard'}, content_type='application/json')
        self.assertEquals(response.status_code, 400)

    def test_detail_GET_data(self):
        self.validClient.post('/board/', {'name': 'TestBoard1'})
        response = self.validClient.get(self.detailUrl)
        self.assertEquals(response.status_code, 200)
        response = self.validClient.get(self.wrongUrl)
        self.assertEquals(response.status_code, 404)

    def test_detail_PUT_data(self):
        self.validClient.post('/board/', {'name': 'PostName Before Update'})
        response = self.validClient.put(self.detailUrl, {'name': 'PostName after Update'}, content_type='application/json')
        self.assertEquals(response.status_code, 200)
        response = self.validClient.put(self.wrongUrl, {'name': 'PostName after Update'}, content_type='application/json')
        self.assertEquals(response.status_code, 404)

    def test_detail_DELETE_data(self):
        self.validClient.post('/board/', {'name': 'TestPostName'}, content_type='application/json')
        response = self.validClient.delete(self.detailUrl)
        self.assertEquals(response.status_code, 204)
        response = self.validClient.delete(self.wrongUrl)
        self.assertEquals(response.status_code, 404)