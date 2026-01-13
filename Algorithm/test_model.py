from django.test import TestCase
from Algorithm.models import capitalTypes,CapitalType

class capitalTypesTest(TestCase):
    """This test case test the CRUD (Create Retrieve Update Delete) functionality of capitalType model"""
    
    def setUp(self):
        self.item = capitalTypes.objects.create(id=1,name='SBA Loan')
    
    def test_get(self):
        self.get = capitalTypes.objects.get(name='SBA Loan')
        self.assertEqual(str(self.get),'SBA Loan')
    
    def test_update(self):
        self.update = capitalTypes.objects.update(id=1,name='Private Equity')
        self.get = capitalTypes.objects.get(id=1)
        self.assertEqual(str(self.get),'Private Equity')
    
    def test_delete(self):
        print('hello')
        Delete_Status = False
        capitalTypes.objects.filter(id=1).delete()
        try:
            self.get2 = capitalTypes.objects.get(id=1)
            print(str(self.get2))
        except:
            Delete_Status = True
        self.assertEqual(Delete_Status,True)

class CapitalTypeTest(TestCase):
    """This test case test the CRUD (Create Retrieve Update Delete) functionality of capitalTypes model which stores algorithm
    matrix, counter list, counter and algorithm status based on Mr. Smith's input in algorithm section of the application."""
    
    def setUp(self):
        self.item1= capitalTypes.objects.create(name='SBA Loan')
        self.item2 =CapitalType.objects.create(
            namec=self.item1,
            matrix_weights = [1,0,1,0,1],
            counterlist = [1,1,1,1,1],
            counter = 3,
            status = True,
            )
    def test_get(self):
        self.get = CapitalType.objects.get(namec=self.item1)
        self.assertEqual(str(self.get),'SBA Loan : 3')
    
    def test_update(self):
        self.update = CapitalType.objects.update(namec=self.item1,counter=2)
        self.get = CapitalType.objects.get(namec=self.item1)
        self.assertEqual(str(self.get),'SBA Loan : 2')
    
    def test_delete(self):
        Delete_Status = False
        CapitalType.objects.filter(namec=self.item1).delete()
        try:
            self.get2 = CapitalType.objects.get(namec=self.item1)
            print(str(self.get2))
        except:
            Delete_Status = True
        self.assertEqual(Delete_Status,True)