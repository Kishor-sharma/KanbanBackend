from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from task_api.models import Task
from board_api.models import Board
from column_api.models import Lanes

# Create your tests here.
class TestTaskView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='abc', email='abc@gmail.com', password='top_secret')
        self.validClient = Client()
        self.validClient.login(username='abc', password='top_secret')
        
        self.url = reverse('tasklist')
        self.urlwithbaord = reverse('taskwithboard', args=[1])
        self.utlwithbaordcolumn = reverse('taskwithboardcolumn', args=[1,1])
        self.detailtaskurl = reverse('detailtask', args=[1])
        self.wrongdetailtaskurl = reverse('detailtask', args=[10])
        self.data = {
            "title": "do task",
            "description": "description",
            "status": "False",
            "boardID": 1,
            "columnID": 1
        }
        self.task = Task.objects.create(title= "do task",
            description= "description",
            status= False,
            boardID= 1,
            columnID= 1
        )
        Board.objects.create(name="TestBoard", userID=self.user.id)
        Lanes.objects.create(name="TODO", index=1)
        Lanes.objects.create(name="INPROGRESS", index=2)

    def test_authorization_fail(self):
        client = Client()
        response = client.get(self.url)
        self.assertEquals(response.status_code, 401)

    def test_GET_dataList(self):
        response = self.validClient.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_GET_data_from_singleBoard(self):
        response = self.validClient.get(self.urlwithbaord)
        self.assertEquals(response.status_code, 200)
    
    def test_GET_data_from_singleBoard_singleCloumn(self):
        response = self.validClient.get(self.utlwithbaordcolumn)
        self.assertEquals(response.status_code, 200)

    def test_POST_Data(self):
        response = self.validClient.post(self.url, self.data, content_type='application/json')
        self.assertEquals(response.status_code, 201)

    def test_POST_invalid_data(self):
        new_data = self.data
        del new_data['title']
        response = self.validClient.post(self.url, new_data, content_type='application/json')
        self.assertEquals(response.status_code, 400)
        new_data["boardID"] = 13
        response = self.validClient.post(self.url, new_data, content_type='application/json')
        self.assertEquals(response.status_code, 405)

    def test_detail_GET_data(self):
        response = self.validClient.get(self.detailtaskurl)
        self.assertEquals(response.status_code, 200)
        response = self.validClient.get(self.wrongdetailtaskurl)
        self.assertEquals(response.status_code, 404)

    def test_detail_PUT_data(self):
        updated_data = self.data
        updated_data['title'] = 'updated description'
        response = self.validClient.put(self.detailtaskurl, updated_data, content_type='application/json')
        self.assertEquals(response.status_code, 200)
        response = self.validClient.put(self.wrongdetailtaskurl, updated_data, content_type='application/json')
        self.assertEquals(response.status_code, 404)
        updated_data['columnID'] = 7
        response = self.validClient.put(self.wrongdetailtaskurl, updated_data, content_type='application/json')
        self.assertEquals(response.status_code, 405)

    def test_detail_DELETE_data(self):
        response = self.validClient.delete(self.detailtaskurl)
        self.assertEquals(response.status_code, 204)
        response = self.validClient.delete(self.wrongdetailtaskurl)
        self.assertEquals(response.status_code, 404)