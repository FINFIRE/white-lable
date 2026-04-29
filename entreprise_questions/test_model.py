from django.test import TestCase
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,EQuestions6,EQuestions7,EQuestions8,DocumentsPrepared,referal_response
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.test import APIClient 



class EQuestions1Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions1.objects.create(
            user=self.user,
            Idea = 0,
            Formation = 0,
            Start_Up = 0,
            Growth = 1,
            M_And_A  = 0,
            Preparing_For_Public = 0,
            Distressed = 0,
            Selected_Option = 'Growth',
            )
        self.assertEqual(str(self.item),'testuser : Growth')
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions1.objects.create(
            user=self.user,
            Idea = 0,
            Formation = 0,
            Start_Up = 0,
            Growth = 1,
            M_And_A  = 0,
            Preparing_For_Public = 0,
            Distressed = 0,
            Selected_Option = 'Growth',
            )
                       
        self.get = EQuestions1.objects.get(user=self.user)
        self.assertEqual(str(self.item),'testuser : Growth')

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions1.objects.create(
            user=self.user,
            Idea = 0,
            Formation = 0,
            Start_Up = 0,
            Growth = 1,
            M_And_A  = 0,
            Preparing_For_Public = 0,
            Distressed = 0,
            Selected_Option = 'Growth',
            )    
        self.update =EQuestions1.objects.update(
            user=self.user,
            Idea = 0,
            Formation = 1,
            Start_Up = 0,
            Growth = 0,
            M_And_A  = 0,
            Preparing_For_Public = 0,
            Distressed = 0,
            Selected_Option = 'Formation',
            )
        self.get = EQuestions1.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : Formation')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions1.objects.create(
            user=self.user,
            Idea = 0,
            Formation = 0,
            Start_Up = 0,
            Growth = 1,
            M_And_A  = 0,
            Preparing_For_Public = 0,
            Distressed = 0,
            Selected_Option = 'Growth',
            )    
        Delete_status = False
        EQuestions1.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions1.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class EQuestionsTest(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.item =EQuestions.objects.create(
            user=self.user,
            RC_zero_to_499 = 1,
            RC_500_to_999 = 0,
            RC_1000_to_2499 = 0,
            RC_2500_to_4999 = 0,
            RC_5000_to_9999  = 0,
            RC_10000_to_24999 = 0,
            RC_25000_to_49999 = 0,
            RC_More_Than_50000 = 0,
            Selected_Option = '0 - $499',
            RT_1D_to_1W = 1,
            RT_1W_to_2W = 0,
            RT_2W_to_4W = 0,
            RT_1M_to_2M  = 0,
            RT_2M_to_3M = 0,
            RT_3M_to_6M = 0,
            RT_6M_to_12M = 0,
            RT_More_Than_a_Year = 0,
            Selected_Option2 = "1 Day to 1 Week",
            )
        self.assertEqual(str(self.item),'testuser : 0 - $499, 1 Day to 1 Week')
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions.objects.create(
            user=self.user,
            RC_zero_to_499 = 1,
            RC_500_to_999 = 0,
            RC_1000_to_2499 = 0,
            RC_2500_to_4999 = 0,
            RC_5000_to_9999  = 0,
            RC_10000_to_24999 = 0,
            RC_25000_to_49999 = 0,
            RC_More_Than_50000 = 0,
            Selected_Option = '0 - $499',
            RT_1D_to_1W = 1,
            RT_1W_to_2W = 0,
            RT_2W_to_4W = 0,
            RT_1M_to_2M  = 0,
            RT_2M_to_3M = 0,
            RT_3M_to_6M = 0,
            RT_6M_to_12M = 0,
            RT_More_Than_a_Year = 0,
            Selected_Option2 = "1 Day to 1 Week",
            )                
        self.get = EQuestions.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : 0 - $499, 1 Day to 1 Week')

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions.objects.create(
            user=self.user,
            RC_zero_to_499 = 1,
            RC_500_to_999 = 0,
            RC_1000_to_2499 = 0,
            RC_2500_to_4999 = 0,
            RC_5000_to_9999  = 0,
            RC_10000_to_24999 = 0,
            RC_25000_to_49999 = 0,
            RC_More_Than_50000 = 0,
            Selected_Option = '0 - $499',
            RT_1D_to_1W = 1,
            RT_1W_to_2W = 0,
            RT_2W_to_4W = 0,
            RT_1M_to_2M  = 0,
            RT_2M_to_3M = 0,
            RT_3M_to_6M = 0,
            RT_6M_to_12M = 0,
            RT_More_Than_a_Year = 0,
            Selected_Option2 = "1 Day to 1 Week",
            )                
        self.update = EQuestions.objects.update(
            user=self.user,
            RC_zero_to_499 = 0 ,
            RC_500_to_999 = 1,
            RC_1000_to_2499 = 0,
            RC_2500_to_4999 = 0,
            RC_5000_to_9999  = 0,
            RC_10000_to_24999 = 0,
            RC_25000_to_49999 = 0,
            RC_More_Than_50000 = 0,
            Selected_Option = '$500 - $999',
            RT_1D_to_1W = 0,
            RT_1W_to_2W = 1,
            RT_2W_to_4W = 0,
            RT_1M_to_2M  = 0,
            RT_2M_to_3M = 0,
            RT_3M_to_6M = 0,
            RT_6M_to_12M = 0,
            RT_More_Than_a_Year = 0,
            Selected_Option2 = "1 Week to 2 Weeks",
            )
        self.get = EQuestions.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : $500 - $999, 1 Week to 2 Weeks')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions.objects.create(
            user=self.user,
            RC_zero_to_499 = 1,
            RC_500_to_999 = 0,
            RC_1000_to_2499 = 0,
            RC_2500_to_4999 = 0,
            RC_5000_to_9999  = 0,
            RC_10000_to_24999 = 0,
            RC_25000_to_49999 = 0,
            RC_More_Than_50000 = 0,
            Selected_Option = '0 - $499',
            RT_1D_to_1W = 1,
            RT_1W_to_2W = 0,
            RT_2W_to_4W = 0,
            RT_1M_to_2M  = 0,
            RT_2M_to_3M = 0,
            RT_3M_to_6M = 0,
            RT_6M_to_12M = 0,
            RT_More_Than_a_Year = 0,
            Selected_Option2 = "1 Day to 1 Week",
            )
        Delete_status = False
        EQuestions.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class EQuestions2Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions2.objects.create(
            user=self.user,
            Business_Name = "Romin Inc.",
            Registration_Region = "Yemen",
            No_Business = 0,
            Sole_Proprietorship = 0,
            LLC  = 1,
            LP = 0,
            GP = 0,
            S_Corporation = 0,
            C_Corp = 0,
            Other = 0,
            Selected_Option = "LLC",
            )
        self.assertEqual(str(self.item),'testuser : LLC')
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions2.objects.create(
            user=self.user,
            Business_Name = "Romin Inc.",
            Registration_Region = "Yemen",
            No_Business = 0,
            Sole_Proprietorship = 0,
            LLC  = 1,
            LP = 0,
            GP = 0,
            S_Corporation = 0,
            C_Corp = 0,
            Other = 0,
            Selected_Option = "LLC",
            )            
        self.get = EQuestions2.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : LLC')

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions2.objects.create(
            user=self.user,
            Business_Name = "Romin Inc.",
            Registration_Region = "Yemen",
            No_Business = 0,
            Sole_Proprietorship = 0,
            LLC  = 1,
            LP = 0,
            GP = 0,
            S_Corporation = 0,
            C_Corp = 0,
            Other = 0,
            Selected_Option = "LLC",
            )              
        self.item =EQuestions2.objects.update(
            user=self.user,
            Business_Name = "Romin Inc.",
            Registration_Region = "Yemen",
            No_Business = 0,
            Sole_Proprietorship = 0,
            LLC  = 0,
            LP = 1,
            GP = 0,
            S_Corporation = 0,
            C_Corp = 0,
            Other = 0,
            Selected_Option = "LP",
            )     
        self.get = EQuestions2.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : LP')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions2.objects.create(
            user=self.user,
            Business_Name = "Romin Inc.",
            Registration_Region = "Yemen",
            No_Business = 0,
            Sole_Proprietorship = 0,
            LLC  = 0,
            LP = 1,
            GP = 0,
            S_Corporation = 0,
            C_Corp = 0,
            Other = 0,
            Selected_Option = "LP",
            )     
        Delete_status = False
        EQuestions2.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions2.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class EQuestions3Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions3.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 1,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_2M = 0,
            More_2M_Less_5M = 0,
            More_5M_Less_10M = 0,
            More_10M = 0,
            Selected_Option = '$101,000 to $250,000',
            )
        self.assertEqual(str(self.item),'testuser : $101,000 to $250,000')
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions3.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 1,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_2M = 0,
            More_2M_Less_5M = 0,
            More_5M_Less_10M = 0,
            More_10M = 0,
            Selected_Option = '$101,000 to $250,000',
            )
        self.get = EQuestions3.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : $101,000 to $250,000')

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions3.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 1,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_2M = 0,
            More_2M_Less_5M = 0,
            More_5M_Less_10M = 0,
            More_10M = 0,
            Selected_Option = '$101,000 to $250,000',
            )         
        self.item =EQuestions3.objects.update(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 0,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_2M = 1,
            More_2M_Less_5M = 0,
            More_5M_Less_10M = 0,
            More_10M = 0,
            Selected_Option = '$1,000,001 to $2,000,000',
            )   
        self.get = EQuestions3.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : $1,000,001 to $2,000,000')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions3.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 0,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_2M = 1,
            More_2M_Less_5M = 0,
            More_5M_Less_10M = 0,
            More_10M = 0,
            Selected_Option = '$1,000,001 to $2,000,000',
            )    
        Delete_status = False
        EQuestions3.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions3.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class EQuestions4Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions4.objects.create(
            user=self.user,
            Accelerator = 0,
            Bonds = 0,
            Comercial_Banking = 1,
            Cryptocurrency = 0,
            EB5_Immigration  = 0,
            Enterprise_Zones = 0,
            Factoring = 0,
            Grants = 0,
            Hedge_Funds = 0,
            Incubator = 0,
            Investment_Banking = 0,
            Other_Owner_Equity = 0,
            Private_Debt = 0,
            Private_Equity = 0,
            Public_Offereing = 0,
            Real_Estate = 0,
            Royalty_Financing = 0,
            Small_Business_Administration = 0,
            Venture_Capital = 0,
            Unsure = 0,
            Selected_Options = 'Commercial Banks',
            )
        self.assertEqual(str(self.item),"testuser : Commercial Banks")
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions4.objects.create(
            user=self.user,
            Accelerator = 0,
            Bonds = 0,
            Comercial_Banking = 1,
            Cryptocurrency = 0,
            EB5_Immigration  = 0,
            Enterprise_Zones = 0,
            Factoring = 0,
            Grants = 0,
            Hedge_Funds = 0,
            Incubator = 0,
            Investment_Banking = 0,
            Other_Owner_Equity = 0,
            Private_Debt = 0,
            Private_Equity = 0,
            Public_Offereing = 1,
            Real_Estate = 0,
            Royalty_Financing = 0,
            Small_Business_Administration = 0,
            Venture_Capital = 0,
            Unsure = 0,
            Selected_Options =['Commercial Banks','Public Offering'],
            )
        self.get = EQuestions4.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : ['Commercial Banks', 'Public Offering']")

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions4.objects.create(
            user=self.user,
            Accelerator = 0,
            Bonds = 0,
            Comercial_Banking = 1,
            Cryptocurrency = 0,
            EB5_Immigration  = 0,
            Enterprise_Zones = 0,
            Factoring = 0,
            Grants = 0,
            Hedge_Funds = 0,
            Incubator = 0,
            Investment_Banking = 0,
            Other_Owner_Equity = 0,
            Private_Debt = 0,
            Private_Equity = 0,
            Public_Offereing = 0,
            Real_Estate = 0,
            Royalty_Financing = 0,
            Small_Business_Administration = 0,
            Venture_Capital = 0,
            Unsure = 0,
            Selected_Options = 'Commercial Banks',
            )  
        self.item =EQuestions4.objects.update(
            user=self.user,
            Accelerator = 0,
            Bonds = 1,
            Comercial_Banking = 0,
            Cryptocurrency = 0,
            EB5_Immigration  = 0,
            Enterprise_Zones = 0,
            Factoring = 0,
            Grants = 0,
            Hedge_Funds = 0,
            Incubator = 0,
            Investment_Banking = 0,
            Other_Owner_Equity = 0,
            Private_Debt = 0,
            Private_Equity = 0,
            Public_Offereing = 0,
            Real_Estate = 0,
            Royalty_Financing = 0,
            Small_Business_Administration = 0,
            Venture_Capital = 0,
            Unsure = 0,
            Selected_Options = "Bonds",
            )
        self.get = EQuestions4.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : Bonds')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions4.objects.create(
            user=self.user,
            Accelerator = 0,
            Bonds = 0,
            Comercial_Banking = 1,
            Cryptocurrency = 0,
            EB5_Immigration  = 0,
            Enterprise_Zones = 0,
            Factoring = 0,
            Grants = 0,
            Hedge_Funds = 0,
            Incubator = 0,
            Investment_Banking = 0,
            Other_Owner_Equity = 0,
            Private_Debt = 0,
            Private_Equity = 0,
            Public_Offereing = 0,
            Real_Estate = 0,
            Royalty_Financing = 0,
            Small_Business_Administration = 0,
            Venture_Capital = 0,
            Unsure = 0,
            Selected_Options = 'Commercial Banks',
            )  
        Delete_status = False
        EQuestions4.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions4.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class EQuestions5Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions5.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 0,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_1_35M = 0,
            More_1_35M_Less_2M = 0,
            More_2M_Less_5M = 1,
            More_5M_Less_10M = 0,
            More_10M_Less_20M = 0,
            More_20M = 0,
            Unsure = 0,
            Selected_Option = '$2,000,000 to $4,999,999',
            )
        self.assertEqual(str(self.item),"testuser : $2,000,000 to $4,999,999")
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions5.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 0,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_1_35M = 0,
            More_1_35M_Less_2M = 0,
            More_2M_Less_5M = 1,
            More_5M_Less_10M = 0,
            More_10M_Less_20M = 0,
            More_20M = 0,
            Unsure = 0,
            Selected_Option = '$2,000,000 to $4,999,999',
            )
        self.get = EQuestions5.objects.get(user=self.user)
        self.assertEqual(str(self.item),"testuser : $2,000,000 to $4,999,999")

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions5.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 0,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 0,
            More_1M_Less_1_35M = 0,
            More_1_35M_Less_2M = 0,
            More_2M_Less_5M = 1,
            More_5M_Less_10M = 0,
            More_10M_Less_20M = 0,
            More_20M = 0,
            Unsure = 0,
            Selected_Option = '$2,000,000 to $4,999,999',
            )
        self.item =EQuestions5.objects.update(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 0,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 1,
            More_1M_Less_1_35M = 0,
            More_1_35M_Less_2M = 0,
            More_2M_Less_5M = 0,
            More_5M_Less_10M = 0,
            More_10M_Less_20M = 0,
            More_20M = 0,
            Unsure = 0,
            Selected_Option = '$500,000 to $999,999',
            )
        self.get = EQuestions5.objects.get(user=self.user)
        self.assertEqual(str(self.get),'testuser : $500,000 to $999,999')

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions5.objects.create(
            user=self.user,
            Less_25k = 0,
            More_25K_Less_100k = 0,
            More_100k_Less_250K = 0,
            More_250k_Less_500K = 0,
            More_500K_Less_1M  = 1,
            More_1M_Less_1_35M = 0,
            More_1_35M_Less_2M = 0,
            More_2M_Less_5M = 0,
            More_5M_Less_10M = 0,
            More_10M_Less_20M = 0,
            More_20M = 0,
            Unsure = 0,
            Selected_Option = '$500,000 to $999,999',
            )
        Delete_status = False
        EQuestions5.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions5.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class EQuestions6Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions6.objects.create(
            user=self.user,
            Founders_Round = 0,
            Pre_Seed = 0,
            Seed = 0,
            Series_A = 0,
            Series_B  = 0,
            Series_C = 0,
            Pre_Ipo = 0,
            Ipo = 1,
            Unsure = 0,
            Selected_Options = 'IPO',
            One = 0,
            Two = 0,
            TBD = 0,
            Selected_Option = 'One',
            )
        self.assertEqual(str(self.item),"testuser : IPO : One")
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions6.objects.create(
            user=self.user,
            Founders_Round = 0,
            Pre_Seed = 0,
            Seed = 0,
            Series_A = 0,
            Series_B  = 0,
            Series_C = 0,
            Pre_Ipo = 0,
            Ipo = 1,
            Unsure = 0,
            Selected_Options = 'IPO',
            One = 0,
            Two = 0,
            TBD = 0,
            Selected_Option = 'One',
            )
        self.get = EQuestions6.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : IPO : One")

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions6.objects.create(
            user=self.user,
            Founders_Round = 0,
            Pre_Seed = 0,
            Seed = 0,
            Series_A = 0,
            Series_B  = 0,
            Series_C = 0,
            Pre_Ipo = 0,
            Ipo = 1,
            Unsure = 0,
            Selected_Options = 'IPO',
            One = 0,
            Two = 0,
            TBD = 0,
            Selected_Option = 'One',
            )
        
        self.item =EQuestions6.objects.update(
            user=self.user,
            Founders_Round = 0,
            Pre_Seed = 0,
            Seed = 0,
            Series_A = 0,
            Series_B  = 0,
            Series_C = 1,
            Pre_Ipo = 0,
            Ipo = 0,
            Unsure = 0,
            Selected_Options = 'Series C',
            One = 0,
            Two = 0,
            TBD = 0,
            Selected_Option = 'One',
            )
        self.get = EQuestions6.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : Series C : One")

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions6.objects.create(
            user=self.user,
            Founders_Round = 0,
            Pre_Seed = 0,
            Seed = 0,
            Series_A = 0,
            Series_B  = 0,
            Series_C = 1,
            Pre_Ipo = 0,
            Ipo = 0,
            Unsure = 0,
            Selected_Options = 'Series C',
            One = 0,
            Two = 0,
            TBD = 0,
            Selected_Option = 'One',
            )
        Delete_status = False
        EQuestions6.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions6.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True) 

class EQuestions7Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions7.objects.create(
            user=self.user,
            Start_Up = 1,
            Growth_Scalabitlity = 0,
            Marketing_and_Sales = 0,
            Cash_FLow_Capital = 0,
            Human_Capital  = 0,
            Equipment = 0,
            Merger_and_Acquistions = 0,
            Inventory = 0,
            Real_State = 0,
            Other = 0,
            Unsure = 0,
            Selected_Options = 'Startup/Working',
            )
        self.assertEqual(str(self.item),"testuser : Startup/Working")
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions7.objects.create(
            user=self.user,
            Start_Up = 1,
            Growth_Scalabitlity = 0,
            Marketing_and_Sales = 0,
            Cash_FLow_Capital = 0,
            Human_Capital  = 0,
            Equipment = 0,
            Merger_and_Acquistions = 0,
            Inventory = 0,
            Real_State = 0,
            Other = 0,
            Unsure = 0,
            Selected_Options = 'Startup/Working',
            )
        self.get = EQuestions7.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : Startup/Working")

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions7.objects.create(
            user=self.user,
            Start_Up = 1,
            Growth_Scalabitlity = 0,
            Marketing_and_Sales = 0,
            Cash_FLow_Capital = 0,
            Human_Capital  = 0,
            Equipment = 0,
            Merger_and_Acquistions = 0,
            Inventory = 0,
            Real_State = 0,
            Other = 0,
            Unsure = 0,
            Selected_Options = 'Startup/Working',
            )
        
        self.item =EQuestions7.objects.update(
            user=self.user,
            Start_Up = 0,
            Growth_Scalabitlity = 1,
            Marketing_and_Sales = 0,
            Cash_FLow_Capital = 0,
            Human_Capital  = 0,
            Equipment = 0,
            Merger_and_Acquistions = 0,
            Inventory = 0,
            Real_State = 0,
            Other = 0,
            Unsure = 0,
            Selected_Options = 'Growth Scalability',
            )
        self.get = EQuestions7.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : Growth Scalability")

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions7.objects.create(
            user=self.user,
            Start_Up = 1,
            Growth_Scalabitlity = 0,
            Marketing_and_Sales = 0,
            Cash_FLow_Capital = 0,
            Human_Capital  = 0,
            Equipment = 0,
            Merger_and_Acquistions = 0,
            Inventory = 0,
            Real_State = 0,
            Other = 0,
            Unsure = 0,
            Selected_Options = 'Startup/Working',
            )
        Delete_status = False
        EQuestions7.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions7.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class EQuestions8Test(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =EQuestions8.objects.create(
            user=self.user,
            Low_Risk_Tolerance = 1,
            Medium_Risk_Tolerance = 0,
            High_Risk_Tolerance = 0,
            Selected_Option = 'Very Low/Low Risk Tolerance (Expect to at least recoup principle)',
            Low_Cost_Capital = 1,
            Medium_Cost_Capital  = 0,
            High_Cost_Capital = 0,
            Very_High_Cost_Capital = 0,
            Immaterial_Cost_Capital = 0,
            Selected_Option2 = 'Low Cost of Capital (1-4%)',
            )
        self.assertEqual(str(self.item),"testuser : Very Low/Low Risk Tolerance (Expect to at least recoup principle) : Low Cost of Capital (1-4%)")
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions8.objects.create(
            user=self.user,
            Low_Risk_Tolerance = 1,
            Medium_Risk_Tolerance = 0,
            High_Risk_Tolerance = 0,
            Selected_Option = 'Very Low/Low Risk Tolerance (Expect to at least recoup principle)',
            Low_Cost_Capital = 1,
            Medium_Cost_Capital  = 0,
            High_Cost_Capital = 0,
            Very_High_Cost_Capital = 0,
            Immaterial_Cost_Capital = 0,
            Selected_Option2 = 'Low Cost of Capital (1-4%)',
            )
        self.get = EQuestions8.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : Very Low/Low Risk Tolerance (Expect to at least recoup principle) : Low Cost of Capital (1-4%)")

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions8.objects.create(
            user=self.user,
            Low_Risk_Tolerance = 1,
            Medium_Risk_Tolerance = 0,
            High_Risk_Tolerance = 0,
            Selected_Option = 'Very Low/Low Risk Tolerance (Expect to at least recoup principle)',
            Low_Cost_Capital = 1,
            Medium_Cost_Capital  = 0,
            High_Cost_Capital = 0,
            Very_High_Cost_Capital = 0,
            Immaterial_Cost_Capital = 0,
            Selected_Option2 = 'Low Cost of Capital (1-4%)',
            )
        
        self.item =EQuestions8.objects.update(
            user=self.user,
            Low_Risk_Tolerance = 0,
            Medium_Risk_Tolerance = 1,
            High_Risk_Tolerance = 0,
            Selected_Option = 'Medium Cost of Capital (5-10%)',
            Low_Cost_Capital = 1,
            Medium_Cost_Capital  = 0,
            High_Cost_Capital = 0,
            Very_High_Cost_Capital = 0,
            Immaterial_Cost_Capital = 0,
            Selected_Option2 = 'Low Cost of Capital (1-4%)',
            )
        self.get = EQuestions8.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : Medium Cost of Capital (5-10%) : Low Cost of Capital (1-4%)")

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =EQuestions8.objects.create(
            user=self.user,
            Low_Risk_Tolerance = 1,
            Medium_Risk_Tolerance = 0,
            High_Risk_Tolerance = 0,
            Selected_Option = 'Very Low/Low Risk Tolerance (Expect to at least recoup principle)',
            Low_Cost_Capital = 1,
            Medium_Cost_Capital  = 0,
            High_Cost_Capital = 0,
            Very_High_Cost_Capital = 0,
            Immaterial_Cost_Capital = 0,
            Selected_Option2 = 'Low Cost of Capital (1-4%)',
            )
        Delete_status = False
        EQuestions8.objects.filter(user=self.user).delete()
        try:
            self.get = EQuestions8.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class DocumentsPreparedTest(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item =DocumentsPrepared.objects.create(
            user=self.user,
            summary_of_offering = True,
            financial_forecast = True,
            lean_business_model = True,
            presentation_deck = True,
            leadership_overview = True,
            exit_strategy  = True,
            offering_documents = False,
            ai_generated_deep_dive = True,
            virtual_data_room = True,
            )
        self.assertEqual(str(self.item),"testuser : Summary of offering status is True")
    
    def test_get(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =DocumentsPrepared.objects.create(
            user=self.user,
            summary_of_offering = True,
            financial_forecast = True,
            lean_business_model = True,
            presentation_deck = True,
            leadership_overview = True,
            exit_strategy  = True,
            offering_documents = False,
            ai_generated_deep_dive = True,
            virtual_data_room = True,
            )
        self.get = DocumentsPrepared.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : Summary of offering status is 1")

    def test_update(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =DocumentsPrepared.objects.create(
            user=self.user,
            summary_of_offering = True,
            financial_forecast = True,
            lean_business_model = True,
            presentation_deck = True,
            leadership_overview = True,
            exit_strategy  = True,
            offering_documents = False,
            ai_generated_deep_dive = True,
            virtual_data_room = True,
            )
        
        self.update =DocumentsPrepared.objects.update(
            user=self.user,
            summary_of_offering = True,
            financial_forecast = True,
            lean_business_model = True,
            presentation_deck = True,
            leadership_overview = True,
            exit_strategy  = False,
            offering_documents = False,
            ai_generated_deep_dive = True,
            virtual_data_room = True,
            )
        self.get = DocumentsPrepared.objects.get(user=self.user)
        self.assertEqual(str(self.get),"testuser : Summary of offering status is 1")

    def test_delete(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.item =DocumentsPrepared.objects.create(
            user=self.user,
            summary_of_offering = True,
            financial_forecast = True,
            lean_business_model = True,
            presentation_deck = True,
            leadership_overview = True,
            exit_strategy  = True,
            offering_documents = False,
            ai_generated_deep_dive = True,
            virtual_data_room = True,
            )
        Delete_status = False
        DocumentsPrepared.objects.filter(user=self.user).delete()
        try:
            self.get = DocumentsPrepared.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)

class refferalTest(TestCase):
    def test_create(self):
        self.user = User.objects.create_user(username = 'testuser',password = 'testpass123')
        self.item = referal_response.objects.create(
            user = self.user,
            referral_source = 'friend',
            referrer_name = 'testrefferer',
            referral_other = 'None',
        )
        self.assertEqual(str(self.item),"User : testuser , Referral Source : friend , Referrer Name : testrefferer , Referral Other : None")
    
    def test_get(self):
        self.user = User.objects.create_user(username = 'testuser',password = 'testpass123')
        self.item = referal_response.objects.create(
            user = self.user,
            referral_source = 'friend',
            referrer_name = 'testrefferer',
            referral_other = 'None',
        )
        self.get = referal_response.objects.get(user=self.user)
        self.assertEqual(str(self.get),"User : testuser , Referral Source : friend , Referrer Name : testrefferer , Referral Other : None")
    
    def test_update(self):
        self.user = User.objects.create_user(username = 'testuser',password = 'testpass123')
        self.item = referal_response.objects.create(
            user = self.user,
            referral_source = 'friend',
            referrer_name = 'testrefferer',
            referral_other = 'None',
        )
        self.item = referal_response.objects.update(
            user = self.user,
            referral_source = 'advisor',
            referrer_name = 'testrefferer',
            referral_other = 'None',
        )
        self.get = referal_response.objects.get(user=self.user)
        self.assertEqual(str(self.get),"User : testuser , Referral Source : advisor , Referrer Name : testrefferer , Referral Other : None")
    
    def test_delete(self):
        self.user = User.objects.create_user(username = 'testuser',password = 'testpass123')
        self.item = referal_response.objects.create(
            user = self.user,
            referral_source = 'friend',
            referrer_name = 'testrefferer',
            referral_other = 'None',
        )
        Delete_status = False
        referal_response.objects.filter(user=self.user).delete()
        try:
            self.get = referal_response.objects.get(user=self.user)
        except:
            Delete_status = True
        self.assertEqual(Delete_status,True)