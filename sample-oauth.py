from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

client_id = 'herd-client'
client_secret = 'PkJsgOiBo71'

auth = HTTPBasicAuth(client_id, client_secret)
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://oauthdev.homebox.com/auth/v1/tokens', auth=auth)


r = oauth.get('https://herddev-api.homebox.com/reference-data/v1/colors')

print r.json()