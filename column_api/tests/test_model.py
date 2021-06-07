from django.test import TestCase
from django.contrib.auth.models import User
from column_api.models import Lanes

class TestLaneModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='dummy', email='dummy@mail.com', password='top_secret')
        Lanes.objects.create(name="some dummy column", index=1)
        Lanes.objects.create(name="another dummy column", index=2)

    def test_data_in_database(self):
        obj1 = Lanes.objects.get(name='some dummy column')
        obj2 = Lanes.objects.get(name='another dummy column')
        self.assertNotEquals(obj1.id, obj2.id)
        self.assertEquals(obj1.__str__(), 'some dummy column')
        self.assertEquals(obj2.__str__(), 'another dummy column' )
