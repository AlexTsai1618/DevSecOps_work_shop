#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#			INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#
from django.test import TestCase
from django.contrib.auth.models import User
from taskManager.models import UserProfile
import datetime

class UserProfileTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_user_profile_creation(self):
        # Create a UserProfile instance for the test user
        user_profile = UserProfile.objects.create(user=self.user)

        # Check if the UserProfile was created successfully
        self.assertIsNotNone(user_profile)

        # Verify the default values
        self.assertEqual(user_profile.image, "")
        self.assertEqual(user_profile.reset_token, "")
        self.assertTrue(isinstance(user_profile.reset_token_expiration, datetime.datetime))

    def test_user_profile_link_to_user(self):
        # Create a UserProfile instance for the test user
        user_profile = UserProfile.objects.create(user=self.user)

        # Check if the UserProfile is linked to the test user
        self.assertEqual(user_profile.user, self.user)

    def tearDown(self):
        # Clean up the created objects
        self.user.delete()
        user_profile = UserProfile.objects.filter(user=self.user).first()
        if user_profile:
            user_profile.delete()
