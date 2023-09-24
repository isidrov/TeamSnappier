import configparser

# Load configuration file

config = configparser.ConfigParser()
config.read('config.ini')

# Accessing the credentials

client_id = config['api']['client_id']

#Set parameters

redirect_uri = 'urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob'
response_type = 'code'
auth_url = "https://auth.teamsnap.com/oauth/authorize"
test_rule = "authorization_test=true"
scope = "read+write"

# Build auth full URL to be launched on a web session with an authenticated user
def print_url():

    full_url = f"{auth_url}?{test_rule}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}"

    print(full_url)


# Call the function

print_url()

### Click the URL provided

### Authenticate if you haven't done so

### Copy the the Authorization Code and copy it inside config.ini


