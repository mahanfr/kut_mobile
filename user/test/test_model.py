from django.test import TestCase
from user.models import User
from django.core.validators import ValidationError


class UserTestCase(TestCase):

    # Create a user model in setUp
    def setUp(self):
        self.user = User(id=1, email='example@gmail.com', phone_number='09354567877', password='12345')

    # Check if model can insert into db
    def test_model_created(self):
        User.objects.create(email='example@gmail.com', phone_number='09354567898', password='12345')
        example_user = User.objects.get(email='example@gmail.com')
        self.assertIsNotNone(self, example_user)
        example_user.delete()

    # Check if Email Validators Raise Error
    def test_user_email_validation(self):
        self.user.email = 'example213gmail.com'
        self.assertRaises(ValidationError, self.user.full_clean)

    # Check if Phonenumber Validators Raise Error
    def test_user_phone_number_validation(self):
        self.user.phone_number = '3333'
        self.assertRaises(ValidationError, self.user.full_clean)
