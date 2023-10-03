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

## Obtain Authorization Tokens

- Make sure you have set your client_id and client_secret on your config.ini file
- Run step1_get_code.py and copy the URL printed.
- Make sure on your default browser you are already logged in with your TeamSnap administrator.
- Paste the URL from Step1 in the browser, it will show an Authorization Token
- Copy the Authorization Token from the previous step in the config.ini, auth_code variable
- Run step2_get_token.py, it will print out your Access Token.
- Copy your Access Token in your config.ini file, access_token variable.


## Example Usage

``` python 
from TeamSnapAPI import TeamSnapAPI

# Create an instance of the TeamSnapAPI class
api = TeamSnapAPI()

# Return a list with a dict with all about myself
myself = api.find_me()

# Print relevant information about myself
variables = ['email', 'id', 'first_name', 'last_name','managed_division_ids']
api.print_list(myself, variables)

# Obtain user_id and division_id
user_id = myself[0]['id']
managed_division_id = myself[0]['managed_division_ids'][0]

# Return Teams I belong
teams_I_belong = api.list_teams(userid)

# Print list of Teams with information I am interested in
variables = ['name','id','division_name','division_id']
api.print_list(teams_I_belong,variables)

# Print division details
division = api.list_divisions(divisionid=managed_division_id)
variables = ['name', 'id', 'league_url']
api.print_list(division, variables)

# List division locations
division_locations = api.list_division_locations(divisionid=managed_division_id)
variables = ['id', 'name']
api.print_list(division_locations, variables)

# Export locations
api.json_to_csv(division_locations,'division_locations_exported.csv')

# Find my team_id
my_team_id = ''
for team in teams_I_belong:
    if team['name'] == 'Edel. Volunteer (test) Team':
        my_team_id = team['id']

# Obtain Events scheduled in a team. you could also query based on userid
events_list = api.list_events(teamid=my_team_id)

# Export opponents of my team
opponents = api.list_opponents(teamid=my_team_id)
api.json_to_csv(opponents, 'opponents_exported.csv')

```
# Bulking data

- Under folder Templates, there are CSV files that are used to import data.
- Copy any template to the root folder to use it for data bulk.


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

