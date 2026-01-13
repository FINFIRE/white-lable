from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from registration.models import UserDetail,UserDetail2

class UserDetailTest(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail.objects.create(
            user = self.user,
            First_Name = "test",
            Middle_Name = "testMid",
            Last_Name = "testLast",
            Affiliation = "Board member",
            User_Email = "test@test.com",
            Company_Website = "www.test.com",
            Business_Adress = "test , test 2051920",
            Business_Phone = "2051920",
            Mobile_Phone = "2051920",
            #Special_Programs =     
        )
        self.assertEqual(str(self.item),'test testLast')
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail.objects.create(
            user = self.user,
            First_Name = "test",
            Middle_Name = "testMid",
            Last_Name = "testLast",
            Affiliation = "Board member",
            User_Email = "test@test.com",
            Company_Website = "www.test.com",
            Business_Adress = "test , test 2051920",
            Business_Phone = "2051920",
            Mobile_Phone = "2051920",
            #Special_Programs =     
        )
        self.get = UserDetail.objects.get(user=self.user)
        self.assertEqual(str(self.item),'test testLast')
    
    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail.objects.create(
            user = self.user,
            First_Name = "test",
            Middle_Name = "testMid",
            Last_Name = "testLast",
            Affiliation = "Board member",
            User_Email = "test@test.com",
            Company_Website = "www.test.com",
            Business_Adress = "test , test 2051920",
            Business_Phone = "2051920",
            Mobile_Phone = "2051920",
            #Special_Programs =     
        )
        self.update = UserDetail.objects.update(
            user = self.user,
            First_Name = "Newtest",
            Middle_Name = "testMid",
            Last_Name = "testLast",
            Affiliation = "Board member",
            User_Email = "test@test.com",
            Company_Website = "www.newtest.com",
            Business_Adress = "test , test 2051920",
            Business_Phone = "2051920",
            Mobile_Phone = "2051920",
            #Special_Programs =     
        )
        self.get = UserDetail.objects.get(user=self.user)
        self.assertEqual(str(self.get),'Newtest testLast')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail.objects.create(
            user = self.user,
            First_Name = "test",
            Middle_Name = "testMid",
            Last_Name = "testLast",
            Affiliation = "Board member",
            User_Email = "test@test.com",
            Company_Website = "www.test.com",
            Business_Adress = "test , test 2051920",
            Business_Phone = "2051920",
            Mobile_Phone = "2051920",
            #Special_Programs =     
        )
        Delete_Status = False
        UserDetail.objects.filter(user=self.user).delete()
        try:
            self.get = UserDetail.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class UserDetail2Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail2.objects.create(
            user = self.user,
            Account_Type = 'Enterprise/Business',
            Primary_Purpose = "Education - Learn the Capital Markets & Capital Types Available",
            Billing_Option = 'Platinum',    
        )
        self.assertEqual(str(self.item),'testuser : Platinum')
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail2.objects.create(
            user = self.user,
            Account_Type = 'Enterprise/Business',
            Primary_Purpose = "Education - Learn the Capital Markets & Capital Types Available",
            Billing_Option = 'Platinum',    
        )
        self.get = UserDetail2.objects.get(user=self.user)
        self.assertEqual(str(self.item),'testuser : Platinum')
    
    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail2.objects.create(
            user = self.user,
            Account_Type = 'Enterprise/Business',
            Primary_Purpose = "Education - Learn the Capital Markets & Capital Types Available",
            Billing_Option = 'Platinum',    
        )
        self.item = UserDetail2.objects.update(
            user = self.user,
            Account_Type = 'Enterprise/Business',
            Primary_Purpose = "Education - Learn the Capital Markets & Capital Types Available",
            Billing_Option = 'Gold',    
        )
        self.get = UserDetail2.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : Gold')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.item = UserDetail2.objects.update(
            user = self.user,
            Account_Type = 'Enterprise/Business',
            Primary_Purpose = "Education - Learn the Capital Markets & Capital Types Available",
            Billing_Option = 'Gold',    
        )
        Delete_Status = False
        UserDetail2.objects.filter(user=self.user).delete()
        try:
            self.get = UserDetail.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)