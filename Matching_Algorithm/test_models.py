from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from Matching_Algorithm.models import allCapitalMatchValues,Letter_Response
import json 
from Matching_Algorithm.views import Match
from django.test.client import RequestFactory
from registration.models import UserDetail,UserDetail2
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,EQuestions6,EQuestions7,EQuestions8,DocumentsPrepared

class allCapitalMatchValuesTest(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = allCapitalMatchValues.objects.create(
            user = self.user,
            percentage = json.loads("""{"percentage" : "20"}"""),
        )
        self.assertEqual(str(self.item),"testuser : {'percentage': '20'}")
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )

        self.item = allCapitalMatchValues.objects.create(
            user = self.user,
            percentage = json.loads("""{"percentage" : "20"}"""),
        )
        self.get = allCapitalMatchValues.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : {'percentage': '20'}")
    
    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = allCapitalMatchValues.objects.create(
            user = self.user,
            percentage = json.loads("""{"percentage": "20"}"""),
        )
        self.update = allCapitalMatchValues.objects.update(
            user = self.user,
            percentage = json.loads("""{"percentage": "30"}"""),
        )
        self.get = allCapitalMatchValues.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : {'percentage': '30'}")

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = allCapitalMatchValues.objects.create(
            user = self.user,
            percentage = json.loads("""{"percentage": "20"}"""),
        )
        Delete_Status = False
        allCapitalMatchValues.objects.filter(user=self.user).delete()
        try:
            self.get = allCapitalMatchValues.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class letterResponseTestExistingUser(TransactionTestCase):
    """This class is a test case for Retrieving JSON response for users whose
    response is already filled in the form and data are present in database. setUp method is loading the data."""
    

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='rominadmin',
            password='test123',  # Django will hash this automatically
            email='rominadmin@example.com',  # Add required fields
        )
        self.item = Letter_Response.objects.create(
            user=self.user,
            firstname = 'romin',
            lastname = 'neupane',
            address = 'jatigal',
            phone = '9823645771',
            email = 'romin@gmail.com',
            businessname  = 'romin enterprise',
            count = '3',
            fundgoal = '2000',
            totalnum = 3,
            cm1name = 'cryptocurrency',
            cm2name = 'tokenization',
            cm3name = 'investment banking',
            cm4name = 'royalty financing',
            cm5name = 'commercial banking',
            cm6name = 'sba',
            cm1no = 2,
            cm2no = 3,
            cm3no = 2,
            cm4no = 3,
            cm5no = 3,
            cm6no = 3,
            intermediaries =3 ,
            price =123 ,
            totalprice =12333 ,
            discount =233 ,
            balancedue =444 ,
            top_6_name = json.loads("""{"percentage" : "20"}""") ,
            top_6_name_output = json.loads("""{"percentage" : "20"}"""),
            infocm1 = 'Long text' ,
            infocm2 = 'Long text' ,
            infocm3 = 'Long text' ,
            infocm4 = 'Long text' ,
            infocm5 = 'Long text' ,
            infocm6 = 'Long text',
            )
                
    def test_get(self):
        # Create a mock request
        factory = RequestFactory()
        request = factory.get('/')
        request.user = self.user
        
        # Call the Match function
        response = Match(request)
        
        # Get the response from database
        self.get = Letter_Response.objects.get(user=self.user)
        self.assertEqual(str(self.get), 'rominadmin : cryptocurrency : tokenization : investment banking')
    
    def test_update(self):
        self.update = Letter_Response.objects.update(
            user=self.user,
            firstname = 'Romin',
            lastname = 'neupane',
            address = 'jatigal',
            phone = '9823645771',
            email = 'romin@gmail.com',
            businessname  = 'romin enterprise',
            count = '3',
            fundgoal = '2000',
            totalnum = 3,
            cm1name = 'Incubator',
            cm2name = 'tokenization',
            cm3name = 'investment banking',
            cm4name = 'royalty financing',
            cm5name = 'commercial banking',
            cm6name = 'sba',
            cm1no = 2,
            cm2no = 3,
            cm3no = 2,
            cm4no = 3,
            cm5no = 3,
            cm6no = 3,
            intermediaries =3 ,
            price =123 ,
            totalprice =12333 ,
            discount =233 ,
            balancedue =444 ,
            top_6_name = json.loads("""{"percentage" : "20"}""") ,
            top_6_name_output = json.loads("""{"percentage" : "20"}"""),
            infocm1 = 'Long text' ,
            infocm2 = 'Long text' ,
            infocm3 = 'Long text' ,
            infocm4 = 'Long text' ,
            infocm5 = 'Long text' ,
            infocm6 = 'Long text',
            )
        self.get2 = Letter_Response.objects.get(user=self.user)
        self.assertEqual(str(self.get2), 'rominadmin : Incubator : tokenization : investment banking')
    
    def test_delete(self):
        Delete_Status = False
        Letter_Response.objects.filter(user=self.user).delete()
        try:
            self.get3 = Letter_Response.objects.get(user=self.user)
        except:
            Delete_Status = True
        self.assertEqual(Delete_Status,True)