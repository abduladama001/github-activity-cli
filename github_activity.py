#!/usr/bin/env python3

import sys
import urllib.request
import urllib.error
import json

username = input("Enter the Github username: ").strip()

if not username:
    print("You must provide a Github username.")
    exit(1)

url = f"https://api.github.com/users/{username}/events"

print(url)

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "github-activity-cli"}
    )

    with urllib.request.urlopen(request) as response:
        data = response.read()
        events = json.loads(data)

except urllib.error.HTTPError as e:
    if e.code == 404:
        print("user not found.")
    elif e.code == 403:
        print("API rate limit exceeded.")
    else:
        print("Failed to fetch data.")
    sys.exit(1)

except urllib.error.URLError:
    print("Network error.")
    sys.exit(1)
finally:
    print("Request completed.")

if len(events) == 0:
    print("No recent activity found.")
    sys.exit(0)

for event in events[:10]:
    event_type = event.get("type")
    repo_name = event.get("repo", {}).get("name")

    if event_type == "PushEvent":
        commits = event.get("payload", {}).get("commits", [])
        print(f"-Pushed {len(commits)} commits to {repo_name}")

    elif event_type == "IssuesEvent":
        action = event.get("payload", {}).get("action")
        if action == "opened":
            print(f"-Opened a new issue in {repo_name}")

    elif event_type == "WatchEvent":
        print(f"- Starred {repo_name}")

    else:
        print(f"- Did {event_type} in {repo_name}")

