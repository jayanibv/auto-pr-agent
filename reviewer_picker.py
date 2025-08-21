def pick_reviewers(diff):
    reviewers = set()
    for file in diff["files"]:
        if file.endswith(".py"):
            reviewers.add("backend-dev")
        elif file.endswith(".js") or file.endswith(".jsx"):
            reviewers.add("frontend-dev")
        else:
            reviewers.add("general-reviewer")
    return list(reviewers)