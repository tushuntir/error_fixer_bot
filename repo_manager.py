import os, subprocess, shutil

REPO_DIR = "repo"
SNAPSHOT = ".snapshot"

def run(cmd):
    subprocess.run(cmd, check=True)

def snapshot():
    if os.path.exists(SNAPSHOT):
        shutil.rmtree(SNAPSHOT)
    shutil.copytree(REPO_DIR, SNAPSHOT)

def rollback():
    shutil.rmtree(REPO_DIR)
    shutil.copytree(SNAPSHOT, REPO_DIR)

def setup(repo_url, token):
    if not os.path.exists(REPO_DIR):
        run(["git","clone",repo_url.replace("https://",f"https://{token}@"),REPO_DIR])