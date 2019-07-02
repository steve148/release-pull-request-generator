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

Running the script requires the following arguments to be passed in as command line arguments.

* **repository_name**: The full name of the repository to create the release pull request for.
* **github_token**: The peronsal access token required to authenticate on github. Check out (https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) for more details on how to create the token.

To create a release pull request for a particular repository following the gitflow model, run the following command.

```shell
pipenv run python release_pull_request_generator.py <repository_name> <github_token>
```

As an example, if I wanted to create a release pull request for a repository called `world_domination_plans` for an organization called `chum_bucket` and I had a personal access token of `1234abcd`, then I would run the following command in my terminal.

```shell
pipenv run python release_pull_request_generator.py chum_bucket/world_dominations_plans 1234abcd
```
