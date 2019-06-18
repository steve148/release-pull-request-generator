from datetime import date
import re


def is_merge_commit(message):
    message_regex = "^Merge pull request #(\d+).*\n\n(.*)$"
    message_pattern = re.compile(merge_commit_message_regex)

    return message_pattern.match(message)


def commit_changelog_message(commit):
    return "* lennoxstevenson: #1234 - Pull Request title"


def __pull_request_body(repository, base, head):
    print()

    compare = repository.compare(base, head)

    print(compare.commits[0].commit.message)

    merge_commits = [
        commit
        for commit in compare.commits
        if is_merge_commit_message(commit.commit.message)
    ]

    print(merge_commits)

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

