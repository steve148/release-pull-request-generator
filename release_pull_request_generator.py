import sys

from github import Github
from parse_command_line_arguments import parse_command_line_arguments
from pull_request_fields import pull_request_fields
from create_release_branch import create_release_branch


def main():
    master_branch_name = "master"
    develop_branch_name = "develop"

    args = parse_command_line_arguments(sys.argv[1:])

    github = Github(args.github_token)

    repository = github.get_repo(args.repository_name)

    release_branch_name = create_release_branch(repository, develop_branch_name)

    fields = pull_request_fields(repository, master_branch_name, release_branch_name)

    repository.create_pull(
        title=fields["title"],
        body=fields["body"],
        base=master_branch_name,
        head=release_branch_name,
    )


if __name__ == "__main__":
    main()
