from branch_monitor import check_new_branches
from diff_analyzer import analyze_diff, classify_pr_type
from pr_composer import compose_pr
from reviewer_picker import pick_reviewers
from pr_creator import create_pr
from labeler import apply_label, comment_reason
from config import REPO_OWNER, REPO_NAME
from utils import log

def run_agent():
    log("Agent started.")
    branches = check_new_branches()
    if not branches:
        log("No new feature branches found.")
        return

    for branch in branches:
        log(f"Processing branch: {branch}")
        diff = analyze_diff(branch)
        pr_data = compose_pr(branch, diff)
        reviewers = pick_reviewers(diff)
        pr_number, commit_msg, diff_text = create_pr(branch, pr_data, reviewers)

        label = classify_pr_type(diff_text, commit_msg)
        apply_label(f"{REPO_OWNER}/{REPO_NAME}", pr_number, label)
        reason = f"Commit message contains '{commit_msg}' and diff includes keywords suggesting a {label}."
        comment_reason(f"{REPO_OWNER}/{REPO_NAME}", pr_number, label, reason)
        log(f"PR #{pr_number} labeled as {label} with reasoning.")