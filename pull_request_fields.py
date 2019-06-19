from datetime import date
import re


MERGE_COMMIT_MESSAGE_REGEX = r"^Merge pull request #(\d+).*\n\n(.*)$"
MERGE_COMMIT_MESSAGE_PATTERN = re.compile(MERGE_COMMIT_MESSAGE_REGEX)


def matches_merge_commit_pattern(message):
    return MERGE_COMMIT_MESSAGE_PATTERN.match(message)


def commit_changelog_message(commit):
    pull_request_number, pull_request_title = matches_merge_commit_pattern(
        commit.commit.message
    ).groups()
    author = commit.author

    return "* {author}: #{pull_request_number} - {pull_request_title}".format(
        author=author,
        pull_request_number=pull_request_number,
        pull_request_title=pull_request_title,
    )


def __pull_request_body(repository, base, head):
    compare = repository.compare(base, head)

    merge_commits = [
        commit
        for commit in compare.commits
        if matches_merge_commit_pattern(commit.commit.message)
    ]

    pull_request_body_lines = ["# Changelog"]

    pull_request_body_lines.extend(
        [commit_changelog_message(commit) for commit in merge_commits]
    )

    return "\n".join(pull_request_body_lines)


def pull_request_fields(repository, head):
    title = "Release {today}".format(today=date.today())
    base = "master"

    body = __pull_request_body(repository, base, head)

    return {"title": title, "body": body, "base": base, "head": head}
