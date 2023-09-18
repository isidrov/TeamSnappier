import requests
import configparser

# Load configuration file

config = configparser.ConfigParser()
config.read('config.ini')

# Accessing authorization token

oauth_token= config['api']['oauth_token']
client_id = config['api']['client_id']
client_secret = config['api']['client_secret']

# Obtain the code  from build_auth_url and paste it below

redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
response_type = 'code'
auth_url = "https://auth.teamsnap.com/oauth/token"
#test_rule = "authorization_test=true"
scope = "read+write"
def get_token():

    # Parameters (you should fill these in with actual values)
    params = {
        'code': oauth_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
        # Add other parameters here
    }

    # Making a POST request
    response = requests.post(auth_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request was successful!")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


# Call the function

get_token()
