import unittest
from unittest.mock import patch, Mock
from src.api.x_client import get_user_id

class TestXClient(unittest.TestCase):

    @patch("src.api.x_client.requests.get")
    def test_get_user_id_dynamic_input(self, mock_get):
        # Mock the API response dynamically
        def mock_response(url, headers):
            username = url.split("/")[-1]
            return Mock(json=lambda: {"data": {"id": f"{username}_id"}}, raise_for_status=Mock())

        mock_get.side_effect = mock_response

        usernames = ["user1", "user2", "anotheruser"]
        for name in usernames:
            user_id = get_user_id(name)
            self.assertEqual(user_id, f"{name}_id")

if __name__ == "__main__":
    unittest.main()
