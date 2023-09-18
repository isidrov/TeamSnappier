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

        print("Request was successful!")

        parsed_json = response.json()
        user_id = parsed_json["collection"]["items"][0]["data"][00]["value"]

        return user_id

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def get_url(url):

    API_HREF = url

    response = requests.get(API_HREF, headers=headers)

    if response.status_code == 200:

        print("Request was successful!")

        parsed_json = response.json()

        print(json.dumps(parsed_json, indent=4))

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def members():

    API_HREF = "https://api.teamsnap.com/v3/members"  # Replace with your endpoint URL

    response = requests.get(API_HREF, headers=headers)

    if response.status_code == 200:

        print("Request was successful!")
        parsed_json = response.json()

        print(json.dumps(parsed_json["collection"]["items"][0]["data"], indent=4))

        user_id = parsed_json["collection"]["items"][0]["data"][00]["value"]

        return user_id

        #for item in parsed_json["collection"]["items"][0]["data"]:
            #print(json.dumps(item, indent=4))

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def divisions():

    API_HREF = "https://api.teamsnap.com/v3/divisions"  # Replace with your endpoint URL

    response = requests.get(API_HREF, headers=headers)

    if response.status_code == 200:

        print("Request was successful!")
        parsed_json = response.json()

        for division in parsed_json:
            print(division['name'])

        #for item in parsed_json["collection"]["items"][0]["data"]:
            #print(json.dumps(item, indent=4))

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def list_teams(userid):

    API_HREF = f"https://api.teamsnap.com/v3/teams/search?user_id={userid}"
    print(API_HREF)
    response = requests.get(API_HREF, headers=headers)

    if response.status_code == 200:

        print("Request was successful!")
        parsed_json = response.json()

        list_of_teams = []

        for team_item in parsed_json["collection"]["items"]:
            team_data = team_item["data"]
            team = {}
            for item in team_data:
                team[item["name"]] = item["value"]

            list_of_teams.append(team)

        return list_of_teams

        #for item in parsed_json["collection"]["items"][0]["data"]:
            #print(json.dumps(item, indent=4))

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def search_user(userid):

    API_HREF = f"https://apiv3.teamsnap.com/users/search?id={userid}"  # Replace with your endpoint URL

    response = requests.get(API_HREF, headers=headers)

    if response.status_code == 200:

        print("Request was successful!")
        parsed_json = response.json()

        print(f"My ID is {parsed_json['collection']['items'][0]['data'][00]['value']}")

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


def create_team_member(member):

    API_HREF = f"https://api.teamsnap.com/v3/members"  # Replace with your endpoint URL

    response = requests.post(API_HREF, headers=headers,json=member)

    if response.status_code == 200:

        print("Request was successful!")
        parsed_json = response.json()

        print(f"My ID is {parsed_json['collection']['items'][0]['data'][00]['value']}")

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def main():

    userid = find_me()

    #search_user(str(userid))

    teams_I_belong = list_teams(str(userid))

    for team in teams_I_belong:
        print(f"Team Name: {team['name']}\nTeam Id: {team['id']}")
        print("\n")

    data = {
        "template": {
            "data": [
                {"name": "first_name", "value": "Jane"},
                {"name": "last_name", "value": "Doe"},
                {"name": "team_id", "value": 8780519}
            ]
        }
    }

    create_team_member(data)
    #get_url("https://api.teamsnap.com/v3/events")


if __name__ == "__main__":

    main()
