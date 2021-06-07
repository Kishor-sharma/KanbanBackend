from django.test import TestCase
from django.contrib.auth.models import User
from board_api.models import Board

# Create your tests here.
class BoardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="myth", email="kishorkmr2002@gmail.com", password="top_secret")
        Board.objects.create(name="TestBoard", userID=self.user.id)
        Board.objects.create(name="TestBoard1", userID=self.user.id)

    def test_data_in_datebase(self):
        """check if the data was successfully added to the database or not"""
        testboard = Board.objects.get(name="TestBoard")
        testboard1 = Board.objects.get(name="TestBoard1", userID=self.user.id)
        self.assertEqual(testboard.__str__(), "TestBoard")
        self.assertEqual(testboard1.__str__(), "TestBoard1")