# pyTeamSnapAPI

A simple Python API client for TeamSnap.

## Description

The `pyTeamSnapAPI` class provides an easy-to-use Python interface to communicate with TeamSnap's API. This allows developers to interact with TeamSnap's endpoints, such as retrieving the current user's information, listing teams, searching for users, and more.

## Prerequisites

Before using this API class, ensure you have the following:

- **Python installed**: (preferably Python 3.6 or newer).
- The **requests** library installed.
- A configuration file named **config.ini** in the same directory with the following format:

``` ini
[api]
client_id = YOUR_CLIENT_ID
client_Secret = YOUR_CLIENT_SECRET
oauth_code =  AUTHORIZATION_TOKEN_OBTAINED_IN_STEP_1
access_token = ACCESS_TOKEN_OBTAINED_IN_STEP_2
```
- You can obtain your client_id and client_secret at [Team Snap App registration](https://auth.teamsnap.com)
- Make sure one of the Callback URL is urn:ietf:wg:oauth:2.0:oob

## Example Usage

``` python 
from TeamSnapAPI import TeamSnapAPI

# Create an instance of the TeamSnapAPI class
api = TeamSnapAPI()

# Find my own user's ID
userid = api.find_me()
print(f"My user ID is: {userid}")

# Return Teams I belong
teams_I_belong = api.list_teams(userid)

# Print Teams with all its variables
api.print_list(teams_I_belong)

# Print list of Teams with specific variables only
variables = ['name','id','division_name','division_id']
api.print_list(teams_I_belong,variables)

# Obtain Events scheduled in a team
events_list = api.list_events(teamid=1234567)

# Print Events with all its variables
api.print_list(events_list)

# Print Events with specific variables
variables = ['name', 'location_name', 'id', 'type','is_game']
api.print_list(events_list,variables)

```


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

