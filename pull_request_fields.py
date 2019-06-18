from datetime import date


def title():
    return "Release {today}".format(today=date.today())


def pull_request_fields(repository):
    body = ""
    base = ""
    head = ""

    return {"title": title(), "body": body, "base": base, "head": head}

