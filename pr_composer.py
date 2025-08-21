def compose_pr(branch, diff):
    title = f"Auto-PR: Changes in {branch}"
    body = "### Summary\nThis PR includes changes to:\n" + "\n".join(f"- {f}" for f in diff["files"])
    body += f"\n\nBranch: `{branch}`\nBase: `{diff['base']}`"
    return {"title": title, "body": body}