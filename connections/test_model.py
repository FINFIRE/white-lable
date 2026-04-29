from django.test import TestCase
from connections.models import Match_Data
from django.contrib.auth.models import User

class matchDataTest(TestCase):
    """This test case test the Match Data model which stores rendered html code for the final letter which would be
    later turned into pdf or used in other displays in the web  application."""

    def setUp(self):
        self.user = User.objects.create_user(
            username = 'testuser',
            password ='test123',
        )
        item = Match_Data.objects.create(
            user=self.user,
            html ='<html><h1>Test Doc!</h1></html>',
        )
    
    def test_get(self):
        self.get = Match_Data.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : <')
    
    def test_update(self):
        self.update = Match_Data.objects.update(user=self.user,html='!<')
        self.get = Match_Data.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : !')
    
    def test_delete(self):
        Delete_Status = False
        Match_Data.objects.filter(user=self.user).delete()
        try:
            self.get = Match_Data.objects.get(user=self.user)
        except:
            Delete_Status = True
        self.assertEqual(Delete_Status,True)