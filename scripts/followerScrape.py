from instaclient import InstaClient
from instaclient.errors.common import *

# create the client object
client = InstaClient(driver_path='/usr/local/bin/chromedriver')

# log in with your Instagram credentials
try:
  client.login(username='n.titz', password='77kinder')
except SecurityCodeRequired:
  # In case you have 2FA turned on in your IG account
  # Check for the security code in your Authenticator App or via SMS
  code = input('Enter your 2FA security code here: ')
  client.input_security_code(code)

# Scrape Instagram followers
username = input('Enter an instagram account\'s username to scrape it\'s followers: ')
try:
  # This will try to get the user's first 100 followers
  followers = client.scrape_followers(user=username, count=150, callback_frequency=15)
  print(followers)
except InvalidUserError:
  # Exception raised if the username is not valid
  print('The username is not valid')
except PrivateAccountError:
  # Exception raised if the account you are trying to scrape is private
  print('{} is a private account'.format(username))
