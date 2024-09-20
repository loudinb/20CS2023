import unittest
from instagram_clone import InstagramClone
from user import User

class TestInstagramClone(unittest.TestCase):
    def setUp(self):
        self.app = InstagramClone()

    def test_register_user(self):
        user = self.app.register_user("testuser", "test@example.com")
        self.assertIsInstance(user, User)