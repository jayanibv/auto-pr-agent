import subprocess

def check_new_branches():
    result = subprocess.run(["git", "branch", "-r"], capture_output=True, text=True)
    branches = [b.strip().split("/")[-1] for b in result.stdout.splitlines()]
    return [b for b in branches if b.startswith("feature/")]