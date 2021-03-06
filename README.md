# Release Pull Request Generator

> Tool for automated creation of pull requests for releasing changes in the gitflow model.

## Installation

First make sure you have [pipenv](https://github.com/pypa/pipenv) installed for whatever version of python you are running on.

```shell
pipenv --version
```

Then install all the necessary dependencies.

```shell
pipenv install
```

That's it :smiley:

## Usage

Running the script requires the following arguments to be passed in on the command line.

* **repository_name**: The full name of the repository to create the release pull request for.
* **github_token**: The personal access token required to authenticate on github. Check out (https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) for more details on how to create the token.

To create a release pull request for a particular repository following the gitflow model, run the following command.

```shell
pipenv run python release_pull_request_generator.py <repository_name> <your-github-username> <github_token>
```

As an example, if I wanted to create a release pull request for a repository called `world_domination_plans` for an organization called `chum_bucket` and I had a personal access token of `1234abcd`, then I would run the following command in my terminal.

```shell
pipenv run python release_pull_request_generator.py chum_bucket/world_dominations_plans steve148 1234abcd
```

## Assumptions

To figure out which Pull Requests are a part of the release being generated, this script looks for merge commits and infers the pull request fields from that commit. This means if you are rebasing onto develop (eg. no merge commits) then this release generator will not work :( There probably is a smart way to get around this, but for now I went the simple route. Let me know if you have any suggestions!
