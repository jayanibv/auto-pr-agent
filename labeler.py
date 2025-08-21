import requests
from config import GITHUB_TOKEN

def apply_label(repo, pr_number, label):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/labels"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    requests.post(url, json={"labels": [label]}, headers=headers)

def comment_reason(repo, pr_number, label, reason):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    body = f"Labeled as `{label}` because: {reason}"
    requests.post(url, json={"body": body}, headers=headers)