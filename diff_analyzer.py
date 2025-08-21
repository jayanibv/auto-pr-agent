import subprocess

def analyze_diff(branch, base="main"):
    cmd = ["git", "diff", f"{base}...{branch}", "--name-only"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    files = result.stdout.strip().splitlines()
    return {"branch": branch, "base": base, "files": files}

def classify_pr_type(diff_text, commit_msg):
    diff_lower = diff_text.lower()
    msg_lower = commit_msg.lower()
    if "fix" in msg_lower or "bug" in diff_lower:
        return "bug"
    elif "add" in diff_lower or "feature" in msg_lower:
        return "feature"
    elif "refactor" in msg_lower or "refactor" in diff_lower:
        return "refactor"
    elif "test" in diff_lower or "ci" in msg_lower:
        return "chore"
    else:
        return "enhancement"