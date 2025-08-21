import requests
import subprocess
from config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME

def get_latest_commit_msg(branch):
    subprocess.run(["git", "checkout", branch])
    result = subprocess.run(["git", "log", "-1", "--pretty=%B"], capture_output=True, text=True)
    return result.stdout.strip()

def get_diff_text(branch):
    result = subprocess.run(["git", "diff", f"main...{branch}"], capture_output=True, text=True)
    return result.stdout.strip()

def create_pr(branch, pr_data, reviewers):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    payload = {
        "title": pr_data["title"],
        "body": pr_data["body"],
        "head": branch,
        "base": "main"
    }
    response = requests.post(url, json=payload, headers=headers)
    pr_number = response.json().get("number")
    commit_msg = get_latest_commit_msg(branch)
    diff_text = get_diff_text(branch)

    # Assign reviewers
    reviewer_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/requested_reviewers"
    requests.post(reviewer_url, json={"reviewers": reviewers}, headers=headers)

    return pr_number, commit_msg, diff_text