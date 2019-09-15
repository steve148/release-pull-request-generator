import unittest
from unittest.mock import patch, MagicMock
from datetime import date

import create_release_branch


class TestPullRequestFields(unittest.TestCase):
    @patch("create_release_branch.token_hex")
    @patch("create_release_branch.date")
    def test_returns_release_branch_name(self, date_mock, token_hex_mock):

        date_mock.today.return_value = date(2019, 6, 13)
        date_mock.side_effect = lambda *args, **kw: date(*args, **kw)

        token_hex_mock.return_value = "1a2b3c4d"

        repository_mock = MagicMock()

        result = create_release_branch.create_release_branch(
            repository_mock, "develop", "release"
        )

        self.assertEqual(result, "release/2019-06-13-1a2b3c4d")

    @patch("create_release_branch.token_hex")
    @patch("create_release_branch.date")
    def test_creates_new_branch(self, date_mock, token_hex_mock):

        date_mock.today.return_value = date(2019, 6, 13)
        date_mock.side_effect = lambda *args, **kw: date(*args, **kw)

        token_hex_mock.return_value = "1a2b3c4d"

        commit_mock = MagicMock(sha="11111111")

        develop_branch_mock = MagicMock(commit=commit_mock)

        repository_mock = MagicMock()
        repository_mock.get_branch.return_value = develop_branch_mock

        create_release_branch.create_release_branch(
            repository_mock, "develop", "release"
        )

        repository_mock.create_git_ref.assert_called_once_with(
            ref="refs/heads/release/2019-06-13-1a2b3c4d", sha="11111111"
        )


if __name__ == "__main__":
    unittest.main()
