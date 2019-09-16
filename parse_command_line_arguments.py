"""Parsing command line arguments when running main module."""

import argparse


def parse_command_line_arguments(args):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "repository_name",
        help="""
        Name of the github repository you are creating a release pull request for.
        For example, org-name/repo-name
        """,
    )
    parser.add_argument(
        "github_token",
        help="Personal access token with required permissions for creating release.",
    )
    parser.add_argument(
        "--develop-branch",
        default="develop",
        help="Name of the branch you are merging from.",
    )
    parser.add_argument(
        "--master-branch",
        default="master",
        help="Name of the branch that you are merging into.",
    )
    parser.add_argument(
        "--release-branch-prefix",
        default="release",
        help="Prefix of the release branch which will merge into master.",
    )

    return parser.parse_args(args)
