import unittest
from unittest.mock import patch, MagicMock
from datetime import date

import pull_request_fields


def mock_repository(commits=[]):
    commit_mocks = []
    for commit in commits:
        git_commit_mock = MagicMock(message=commit["message"])
        named_user_mock = MagicMock(login=commit["login"])
        commit_mock = MagicMock(commit=git_commit_mock, author=named_user_mock)
        commit_mocks.append(commit_mock)

    comparison_mock = MagicMock(commits=commit_mocks)

    repository_mock = MagicMock()
    repository_mock.compare.return_value = comparison_mock

    return repository_mock


class TestPullRequestFields(unittest.TestCase):
    @patch("pull_request_fields.date")
    def test_title(self, date_mock):
        repository_mock = mock_repository()

        date_mock.today.return_value = date(2019, 6, 13)
        date_mock.side_effect = lambda *args, **kw: date(*args, **kw)

        result = pull_request_fields.pull_request_fields(repository_mock, None, None)

        self.assertEqual(result["title"], "Release 2019-06-13")

    def test_body_no_commits(self):
        repository_mock = mock_repository()

        result = pull_request_fields.pull_request_fields(repository_mock, None, None)

        self.assertEqual(result["body"], "# Changelog")

    def test_body_one_pull_request(self):
        commits = [
            {
                "message": "Merge pull request #1234 from somewhere.\n\nPR title",
                "login": "tonystark",
            }
        ]
        repository_mock = mock_repository(commits=commits)

        result = pull_request_fields.pull_request_fields(repository_mock, None, None)

        self.assertEqual(result["body"], "# Changelog\n* @tonystark: #1234 - PR title")

    def test_body_multiple_pull_requests(self):
        commits = [
            {
                "message": "Merge pull request #1234 from somewhere.\n\nPeanut Butter",
                "login": "tonystark",
            },
            {
                "message": "Merge pull request #5678 from somewhere.\n\nJelly Time",
                "login": "tonystark",
            },
        ]
        repository_mock = mock_repository(commits=commits)

        result = pull_request_fields.pull_request_fields(repository_mock, None, None)

        expected_body = "\n".join(
            [
                "# Changelog",
                "* @tonystark: #1234 - Peanut Butter",
                "* @tonystark: #5678 - Jelly Time",
            ]
        )

        self.assertEqual(result["body"], expected_body)

    def test_reviewers_no_commits(self):
        repository_mock = mock_repository()

        result = pull_request_fields.pull_request_fields(repository_mock, None, None)

        self.assertEqual(result["reviewers"], [])

    def test_reviewers_one_reviewer(self):
        commits = [
            {
                "message": "Merge pull request #1234 from somewhere.\n\nPeanut Butter",
                "login": "tonystark",
            },
            {
                "message": "Merge pull request #5678 from somewhere.\n\nJelly Time",
                "login": "tonystark",
            },
        ]

        repository_mock = mock_repository(commits=commits)

        result = pull_request_fields.pull_request_fields(repository_mock, None, None)

        self.assertEqual(result["reviewers"], ["tonystark"])

    def test_reviewers_mutliple_reviewers(self):
        commits = [
            {
                "message": "Merge pull request #1234 from somewhere.\n\nPeanut Butter",
                "login": "tonystark",
            },
            {
                "message": "Merge pull request #5678 from somewhere.\n\nJelly Time",
                "login": "brucebanner",
            },
        ]

        repository_mock = mock_repository(commits=commits)

        result = pull_request_fields.pull_request_fields(repository_mock, None, None)

        self.assertEqual(set(result["reviewers"]), {"brucebanner", "tonystark"})


if __name__ == "__main__":
    unittest.main()
