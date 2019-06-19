from datetime import date
from secrets import token_hex


def create_release_branch(repository):
    release_branch_name = "release/{release_date}-{unique_hash}".format(
        release_date=date.today(), unique_hash=token_hex(8)
    )

    develop_branch = repository.get_branch("develop")
    repository.create_git_ref(
        ref="refs/heads/{}".format(release_branch_name), sha=develop_branch.commit.sha
    )

    return release_branch_name
