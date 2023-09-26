# 1. Import Statements

import requests
import json
import requests
import configparser

# Load configuration file

config = configparser.ConfigParser()
config.read('config.ini')

# Accessing access token

access_token= config['api']['access_token']

headers = {
    "Authorization": f"Bearer {access_token}"
}

# 2. Function and Class Definitions

def find_me():

    API_HREF = "https://api.teamsnap.com/v3/me"

    response = requests.get(API_HREF, headers=headers)

    if response.status_code == 200:

        print("find_me() was successful!\n")

        parsed_json = response.json()
        user_id = parsed_json["collection"]["items"][0]["data"][00]["value"]

        return user_id

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def write_to_json_file(data, filename="output.json"):
    """
    Write a Python dictionary to a JSON file.

    Parameters:
    - data (dict): The dictionary to write to the file.
    - filename (str): The name of the file to which the data should be written. Defaults to "output.json".

    Returns:
    None
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def get_url(url):

    API_HREF = url

    response = requests.get(API_HREF, headers=headers)

    if response.status_code == 200:

        print("get_url() was successful!\n")

        parsed_json = response.json()

        return parsed_json

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


def list_teams(userid):

    params = {
        'user_id': userid
    }

    API_HREF = f"https://api.teamsnap.com/v3/teams/search"

    response = requests.get(API_HREF, headers=headers, params=params)

    if response.status_code == 200:

        print("list_teams() was successful!\n")
        parsed_json = response.json()

        list_of_teams = []

        for team_item in parsed_json["collection"]["items"]:
            team_data = team_item["data"]
            team = {}
            for item in team_data:
                team[item["name"]] = item["value"]

            list_of_teams.append(team)

        return list_of_teams


    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def search_user(userid):

    params = {
        'id': userid
    }

    API_HREF = f"https://apiv3.teamsnap.com/users/search"  # Replace with your endpoint URL

    response = requests.get(API_HREF, headers=headers, params=params)

    if response.status_code == 200:

        print("search_user() was successful!\n")

        parsed_json = response.json()

        print(f"id: is {parsed_json['collection']['items'][0]['data'][0]['value']}")
        print(f"email: {parsed_json['collection']['items'][0]['data'][5]['value']}")
        print(f"First Name: {parsed_json['collection']['items'][0]['data'][8]['value']}")
        print(f"Last Name: {parsed_json['collection']['items'][0]['data'][10]['value']}\n")

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


def create_team_member(member):

    API_HREF = f"https://api.teamsnap.com/v3/members"  # Replace with your endpoint URL

    response = requests.post(API_HREF, headers=headers,json=member)

    if response.status_code in (200, 201, 204):

        print(f"{response.status_code} request successful!")

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

#https://api.teamsnap.com/v3/events/search?user_id=28819952'

def list_events(userid):

    params = {
        'user_id': userid
    }

    API_HREF = f"https://api.teamsnap.com/v3/events/search"  # Replace with your endpoint URL

    response = requests.get(API_HREF, headers=headers, params=params)

    if response.status_code == 200:

        print("list_events() was successful!")
        parsed_json = response.json()

        myList = []

        for item in parsed_json["collection"]["items"]:
            data = item["data"]
            team = {}
            for subitem in data:
                team[subitem["name"]] = subitem["value"]

            myList.append(team)

        return myList

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def list_members(team_id):

    params = {
        'team_id': team_id
    }

    API_HREF = f"https://api.teamsnap.com/v3/members/search"  # Replace with your endpoint URL

    response = requests.get(API_HREF, headers=headers, params=params)

    if response.status_code == 200:

        print("list_members() was successful!")
        parsed_json = response.json()
        print("n")

        myList = []
        
        for item in parsed_json["collection"]["items"]:
            data = item["data"]
            team = {}
            for subitem in data:
                team[subitem["name"]] = subitem["value"]

            myList.append(team)

        return myList

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def print_members(memberList):

    for member in memberList:
        print(f"First Name: {member['first_name']}")
        print(f"Last Name: {member['last_name']}")
        print(f"Email address: {member['email_addresses']}\n")

def main():

    userid = find_me()
    events_list = list_events(userid)
    write_to_json_file(events_list,filename='events_list.json')

    '''
    events = get_url('https://api.teamsnap.com/v3/events')
    write_to_json_file(events, filename='events.json')
    userid = find_me()
    search_user(userid)
    teams_I_belong = list_teams(userid)

    for team in teams_I_belong:
        print(f"Team Name: {team['name']}\nTeam Id: {team['id']}")
        print("\n")

    list_of_members = list_members(8780519)

    print_members(list_of_members)

    data = {
        "template": {
            "data": [
                {"name": "first_name", "value": "Janette"},
                {"name": "last_name", "value": "Does"},
                {"name": "team_id", "value": 8780519}
            ]
        }
    }

    #create_team_member(data)
    #get_url("https://api.teamsnap.com/v3/events")
    '''

if __name__ == "__main__":

    main()
