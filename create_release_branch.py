from datetime import date
from secrets import token_hex


def create_release_branch(repository, develop_branch_name, release_branch_prefix):
    release_branch_name = "{prefix}/{release_date}-{unique_hash}".format(
        prefix=release_branch_prefix,
        release_date=date.today(),
        unique_hash=token_hex(8),
    )

    develop_branch = repository.get_branch(develop_branch_name)
    repository.create_git_ref(
        ref="refs/heads/{}".format(release_branch_name), sha=develop_branch.commit.sha
    )

    return release_branch_name
