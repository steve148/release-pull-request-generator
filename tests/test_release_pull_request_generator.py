import unittest
from unittest.mock import patch

import release_pull_request_generator


class TestReleasePullRequestGeneratorModule(unittest.TestCase):
    @patch("release_pull_request_generator.parse_command_line_arguments")
    @patch("release_pull_request_generator.Github")
    def test_creates_pull_request(self, github_mock, parse_mock):
        release_pull_request_generator.main()

        github_mock.return_value.get_repo.return_value.create_pull.assert_called_once()


if __name__ == "__main__":
    unittest.main()