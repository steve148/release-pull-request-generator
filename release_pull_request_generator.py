import sys

from github import Github

from create_release_branch import create_release_branch
from parse_command_line_arguments import parse_command_line_arguments
from pull_request_fields import pull_request_fields


def main():
    args = parse_command_line_arguments(sys.argv[1:])

    repository_name = args.repository_name
    github_token = args.github_token
    develop_branch = args.develop_branch
    master_branch = args.master_branch
    release_branch_prefix = args.release_branch_prefix

    github = Github(github_token)

    repository = github.get_repo(repository_name)

    release_branch = create_release_branch(
        repository, develop_branch, release_branch_prefix
    )

    fields = pull_request_fields(repository, master_branch, release_branch)

    pull_request = repository.create_pull(
        title=fields["title"],
        body=fields["body"],
        base=master_branch,
        head=release_branch,
    )

    pull_request.create_review_request(fields["reviewers"])


if __name__ == "__main__":
    main()
