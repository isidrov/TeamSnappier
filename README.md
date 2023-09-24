# TeamSnapAPI

A simple Python API client for TeamSnap.

## Description

The `TeamSnapAPI` class provides an easy-to-use Python interface to communicate with TeamSnap's API. This allows developers to interact with TeamSnap's endpoints, such as retrieving the current user's information, listing teams, searching for users, and more.

## Features

- **Initialize with authentication token**: Get your API token from `config.ini`.
- **User Information**: Fetch the current user's data using `find_me()`.
- **Dynamic API Call**: Fetch any API URL with `get_url(url)`.
- **List Teams**: Get a list of teams associated with a user ID using `list_teams(userid)`.
- **User Search**: Search for a specific user by their ID with `search_user(userid)`.
- **Add Member**: Add a new team member using `create_team_member(member)`.
- **List Events**: View events related to a user with `list_events(userid)`.
- **Team Members**: Fetch a list of members in a team using `list_members(team_id)`.
- **Print Members**: Display information of members using `print_members(memberList)`.
- **Save as JSON**: Store any data into a JSON file using `write_to_json_file(data, filename="output.json")`.

## Usage

1. **Setup**: Clone this repository.
2. **Configuration**: In the root directory, create a `config.ini` file and insert your TeamSnap API access token:
   ```ini
   [api]
   access_token = YOUR_ACCESS_TOKEN_HERE
