from django.test import TestCase, RequestFactory,Client
from registration.models import UserDetail,UserDetail2
from registration.forms import registration_form, registration_form2 ,registration_formS
from registration.views import home,register,login_view,user_logout,registration_form_view,registration_form_view2
from django.contrib.auth.models import User
from django.urls import reverse

class homeTest(TestCase):
    """This test case test the first home page after login in the account, the view should return
    a rendered html content with proper link for a user for all different account i.e Capital Market,
    Enterprise/Business or Intermediaries."""

    def setUp(self):
        self.factory = RequestFactory()
        self.user1 = User.objects.create_user(
            username = 'testuser1',
            password = 'testuser123',
        )
        self.user2 = User.objects.create_user(
            username = 'testuser2',
            password = 'testuser123',
        )        
        self.user3 = User.objects.create_user(
            username = 'testuser3',
            password = 'testuser123',
        )

        self.item = UserDetail2.objects.create(
            user = self.user1,
            Account_Type = 'Capital Market',
            Primary_Purpose = "I Don't Know - TBD",
        )

        self.item1 = UserDetail2.objects.create(
            user = self.user2,
            Account_Type = 'Enterprise/Business',
            Primary_Purpose = "I Don't Know - TBD",
        )

        self.item2 = UserDetail2.objects.create(
            user = self.user3,
            Account_Type = 'Intermediary',
            Primary_Purpose = "I Don't Know - TBD",
        )
    
    def test_home(self):
        request1 = self.factory.get('/')
        request1.user = self.user1
        request2 = self.factory.get('/')
        request2.user2 = self.user2
        request3 = self.factory.get('/')
        request3.user3 = self.user3 
        response1 = home(request1)
        response2 = home(request2)
        response3 = home(request3)
        self.assertIn('text/html', response1['Content-Type'])
        self.assertIn('text/html', response2['Content-Type'])
        self.assertIn('text/html', response3['Content-Type'])        
        if hasattr(response1, 'context_data'):
            self.assertEqual(response1.context_data.get('link'), 'registration_form_view')
        if hasattr(response2, 'context_data'):
            self.assertEqual(response2.context_data.get('link'), 'registration_form_view')
        if hasattr(response3, 'context_data'):
            self.assertEqual(response3.context_data.get('link'), 'registration_form_view')                        

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('registration')  
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }

    def test_required_fields(self):
        response = self.client.post(self.register_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration1.html')
        self.assertContains(response, 'This field is required', count=3)

    def test_successful_registration(self):
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 302)  # Should redirect after success
        self.assertRedirects(response, reverse('home'))  # Check redirection

        # Verify user was created
        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, 'test@example.com')

    def test_password_mismatch(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'wrongpassword'
        invalid_data['password1'] = 'arongpassword'
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration1.html')
        self.assertContains(response,"""The two password fields didn’t match.""")

    def test_invalid_email(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'not-an-email'
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration1.html')
        self.assertContains(response, 'Enter a valid email address')

    def test_duplicate_username(self):
        # Create a user first
        User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        
        # Try registering same username again
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration1.html')
        self.assertContains(response, 'A user with that username already exists')

    def test_duplicate_email(self):
        # Create a user with same email
        User.objects.create_user(username='otheruser', email='test@example.com', password='testpass')
        
        # Try registering same email again
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration1.html')
        self.assertContains(response, 'This email is already registered')