import unittest
from unittest.mock import patch, MagicMock
from datetime import date

import pull_request_fields


class TestPullRequestFields(unittest.TestCase):
    @patch("pull_request_fields.date")
    def test_title(self, date_mock):

        date_mock.today.return_value = date(2019, 6, 13)
        date_mock.side_effect = lambda *args, **kw: date(*args, **kw)

        result = pull_request_fields.pull_request_fields(None)

        self.assertEqual(result["title"], "Release 2019-06-13")


if __name__ == "__main__":
    unittest.main()
