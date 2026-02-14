GitHub Activity CLI

A simple command-line interface tool that fetches and displays a GitHub user's recent activity directly in your terminal.

Features

- Fetch recent activity for any GitHub user
- Display activity in a clean, readable format
- No external dependencies required (uses only Python standard library)
- Proper error handling for invalid usernames and API failures
- Support for multiple event types (pushes, stars, forks, issues, PRs, etc.)

Requirements

- Python 3.6 or higher
- Internet connection to access GitHub API

Installation

1. Clone this repository:
```bash
git clone https://github.com/abduladama001/github-activity-cli.git
cd github-activity-cli
```

2. Make the script executable (optional, Unix/Linux/macOS only):
```bash
chmod +x github_activity.py
```

Usage

Run the script with a GitHub username as an argument:

```bash
python github_activity.py <username>
```

Or, if you made it executable:

```bash
./github_activity.py <username>
```

Examples

```bash
# Fetch activity for user 'kamranahmedse'
python github_activity.py kamranahmedse
```

Sample Output:
```
Fetching activity for user: kamranahmedse...

- Pushed 3 commit(s) to kamranahmedse/developer-roadmap
- Opened an issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- Forked octocat/Hello-World
- Created branch in kamranahmedse/test-repo
```

Supported Event Types

The CLI currently displays the following GitHub event types:

| Event Type | Description |
|------------|-------------|
| `PushEvent` | Commits pushed to a repository |
| `IssuesEvent` | Issues opened, closed, or reopened |
| `WatchEvent` | Repository starred |
| `ForkEvent` | Repository forked |
| `CreateEvent` | Branch or tag created |
| `PullRequestEvent` | Pull request opened, closed, or merged |
| Other events | Displayed with generic event type |

Error Handling

The tool gracefully handles common errors:

- Invalid username: Displays "User not found" message
- Network issues: Shows connection error details
- API rate limiting: Displays HTTP error information
- Missing arguments: Shows usage instructions

Example Error Messages

```bash
# Invalid username
python github_activity.py nonexistentuser123
# Output: Error: User 'nonexistentuser123' not found

# No username provided
python github_activity.py
# Output: Usage: python github_activity.py <username>
```

How It Works

1. Accepts username: Takes GitHub username as command-line argument
2. API Request: Makes HTTP request to `https://api.github.com/users/<username>/events`
3. Parse response: Extracts and formats event data from JSON response
4. Display output: Shows formatted activity in the terminal

API Reference

This tool uses the GitHub Events API:
- Endpoint: `https://api.github.com/users/{username}/events`
- Method: GET
- Authentication: None required (public events only)
- Rate Limit: 60 requests per hour for unauthenticated requests

Learn more: [GitHub Events API Documentation](https://docs.github.com/en/rest/activity/events)

Project Structure

```
github-activity-cli/
│
├── github_activity.py     Main script
└── README.md            This file
```

Code Overview

The script consists of three main functions:

- `fetch_github_activity(username)`: Makes API request and handles errors
- `format_activity(events)`: Parses and formats event data
- `main()`: Entry point that handles command-line arguments

Limitations

- Shows only the most recent events (GitHub API returns up to 30 events)
- Unauthenticated requests have a rate limit of 60 requests/hour
- Only displays public events
- No caching mechanism (fetches fresh data on every request)

Future Enhancements

Potential improvements for future versions:

- [ ] Add authentication for higher rate limits
- [ ] Implement caching to reduce API calls
- [ ] Add color-coded output for better readability
- [ ] Support for filtering by event type
- [ ] Display timestamps for each activity
- [ ] Add limit flag to control number of events shown
- [ ] Export activity to JSON or CSV format

Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

License

This project is open source and available under the [MIT License](LICENSE).

Acknowledgments

- Built as a solution for the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) project from [roadmap.sh](https://roadmap.sh)
- Uses the GitHub REST API

Author

Your Name - [@nerdyextrovert_](https://twitter.com/nerdyextrovert_)

Project Link: [https://github.com/abduladama001/github-activity-cli](https://github.com/abduladama001/github-activity-cli)

Support

If you found this project helpful, please give it a ⭐️!

For questions or issues, please open an issue on GitHub.
