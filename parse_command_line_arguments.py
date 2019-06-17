"""Parsing command line arguments when running main module."""

import argparse


def parse_command_line_arguments(args):

    parser = argparse.ArgumentParser()

    parser.add_argument("repository_name")
    parser.add_argument("github_token")

    return parser.parse_args(args)

