import unittest

from parse_command_line_arguments import parse_command_line_arguments


class TestParseCommandLineArgumentsModule(unittest.TestCase):
    def test_returns_repository_name(self):
        args = parse_command_line_arguments(["user/repository", "abc123"])

        self.assertEqual(args.repository_name, "user/repository")

    def test_returns_github_token(self):
        args = parse_command_line_arguments(["user/repository", "abc123"])

        self.assertEqual(args.github_token, "abc123")

    def test_returns_develop_branch(self):
        args = parse_command_line_arguments(
            ["user/repository", "abc123", "--develop-branch", "test"]
        )

        self.assertEqual(args.develop_branch, "test")

    def test_returns_default_develop_branch(self):
        args = parse_command_line_arguments(["user/repository", "abc123"])

        self.assertEqual(args.develop_branch, "develop")

    def test_returns_master_branch(self):
        args = parse_command_line_arguments(
            ["user/repository", "abc123", "--master-branch", "test"]
        )

        self.assertEqual(args.master_branch, "test")

    def test_returns_default_master_branch(self):
        args = parse_command_line_arguments(["user/repository", "abc123"])

        self.assertEqual(args.master_branch, "master")

    def test_returns_release_branch(self):
        args = parse_command_line_arguments(
            ["user/repository", "abc123", "--release-branch-prefix", "test"]
        )

        self.assertEqual(args.release_branch_prefix, "test")

    def test_returns_default_release_branch(self):
        args = parse_command_line_arguments(["user/repository", "abc123"])

        self.assertEqual(args.release_branch_prefix, "release")


if __name__ == "__main__":
    unittest.main()
