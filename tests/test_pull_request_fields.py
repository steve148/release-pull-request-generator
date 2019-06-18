import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from datetime import date

import pull_request_fields


def mock_repository():
    message_mock = PropertyMock()
    message = "Merge pull request #1 from somewhere.\n\nPull Request title"
    message_mock.return_value = message

    git_commit_mock = MagicMock()
    git_commit_mock.message = message_mock

    commit_mock = MagicMock()
    commit_mock.commit = git_commit_mock

    compare_mock = MagicMock()
    compare_mock.commits = [commit_mock]

    repository_mock = MagicMock()
    repository_mock.compare = compare_mock

    return repository_mock


class TestPullRequestFields(unittest.TestCase):
    @patch("pull_request_fields.date")
    def test_title(self, date_mock):
        repository_mock = mock_repository()

        date_mock.today.return_value = date(2019, 6, 13)
        date_mock.side_effect = lambda *args, **kw: date(*args, **kw)

        result = pull_request_fields.pull_request_fields(repository_mock, None)

        self.assertEqual(result["title"], "Release 2019-06-13")

    def test_base(self):
        repository_mock = mock_repository()

        result = pull_request_fields.pull_request_fields(repository_mock, None)

        self.assertEqual(result["base"], "master")

    def test_head(self):
        repository_mock = mock_repository()

        result = pull_request_fields.pull_request_fields(
            repository_mock, "release-2019-06-14-a1b2c3d4"
        )

        self.assertEqual(result["head"], "release-2019-06-14-a1b2c3d4")

    def test_body_no_commits(self):
        repository_mock = mock_repository()

        result = pull_request_fields.pull_request_fields(repository_mock, None)

        self.assertEqual(result["body"], "# Changelog")

    def test_body_one_commit(self):
        repository_mock = mock_repository()

        result = pull_request_fields.pull_request_fields(repository_mock, None)

        self.assertEqual(
            result["body"], "# Changelog\n* lennoxstevenson: #1234 - Pull Request title"
        )

    def test_body_multiple_commits_one_pull_request(self):
        pass

    def test_body_multiple_commits_multiple_pull_requests(self):
        pass


if __name__ == "__main__":
    unittest.main()
