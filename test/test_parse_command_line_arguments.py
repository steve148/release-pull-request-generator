import unittest

from parse_command_line_arguments import parse_command_line_arguments


class TestParseCommandLineArgumentsModule(unittest.TestCase):
    def test_returns_repository_name(self):
        args = parse_command_line_arguments(["user/repository", "abc123"])

        self.assertEqual(args.repository_name, "user/repository")

    def test_returns_github_token(self):
        args = parse_command_line_arguments(["user/repository", "abc123"])

        self.assertEqual(args.github_token, "abc123")


if __name__ == "__main__":
    unittest.main()
