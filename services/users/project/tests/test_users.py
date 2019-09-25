# services/users/project/tests/test_users.py

import json
import unittest

from project.tests.base import BaseTestCase

class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /ding route behaves correctly."""
        response = self.client.get('/users/ding')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('dong!', data['message'])
        self.assertIn('success', data['status'])

if __name__ == '__main__':
    unittest.main()
