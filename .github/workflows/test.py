import os
import requests


REPO = os.environ.get("REPO")
PR_NUMBER = os.environ.get("PR_NUMBER")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

api_url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}
data = {"body": "LOL HAHAHAH"}


r = requests.post(api_url, headers=headers, json=data)

if r.status_code == 201:
    print("Review comment posted successfully.")
else:
    print(f"Failed to post comment: {r.text}")
