from datetime import date
import re


MERGE_COMMIT_MESSAGE_REGEX = r"^Merge pull request #(\d+).*\n\n(.*)$"
MERGE_COMMIT_MESSAGE_PATTERN = re.compile(MERGE_COMMIT_MESSAGE_REGEX)


def matches_merge_commit_pattern(message):
    return MERGE_COMMIT_MESSAGE_PATTERN.match(message)


def merge_commit_changelog_message(commit):
    (
        merge_commit_pull_request_number,
        merge_commit_pull_request_title,
    ) = matches_merge_commit_pattern(commit.commit.message).groups()

    author_login = commit.author.login

    return "* @{author_login}: #{pull_request_number} - {pull_request_title}".format(
        author_login=author_login,
        pull_request_number=merge_commit_pull_request_number,
        pull_request_title=merge_commit_pull_request_title,
    )


def pull_request_title():
    return "Release {today}".format(today=date.today())


def pull_request_body(merge_commits):
    pull_request_body_lines = ["# Changelog"]

    pull_request_body_lines.extend(
        [merge_commit_changelog_message(commit) for commit in merge_commits]
    )

    return "\n".join(pull_request_body_lines)


def pull_request_reviewers(merge_commits, pull_request_creator):
    author_logins = [commit.author.login for commit in merge_commits]

    unique_logins = set(author_logins)

    unique_logins.discard(pull_request_creator)

    return list(unique_logins)


def pull_request_fields(repository, base, head, pull_request_creator):
    compare = repository.compare(base, head)

    merge_commits = [
        commit
        for commit in compare.commits
        if matches_merge_commit_pattern(commit.commit.message)
    ]

    title = pull_request_title()
    body = pull_request_body(merge_commits)
    reviewers = pull_request_reviewers(merge_commits, pull_request_creator)

    return {"title": title, "body": body, "reviewers": reviewers}
