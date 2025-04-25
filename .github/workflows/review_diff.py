import os
import subprocess
import openai


openai.api_key =os.environ.get("OPENAPI_KEY")

REPO = os.environ.get("REPO")
PR_NUMBER = os.environ.get("PR_NUMBER")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

diff = subprocess.check_output(
    ["git", "diff", "origin/master...HEAD"],
    text=True
)

if not diff.strip():
    exit(0)

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Ты — опытный код-ревьюер. Проанализируй изменения и предложи улучшения."},
        {"role": "user", "content": f"Вот diff:\n\n{diff}"}
    ]
)
review_comment = response.choices[0].message.content

print(review_comment)
