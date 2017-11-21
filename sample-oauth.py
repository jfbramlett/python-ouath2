from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

client_id = 'given-client-id'
client_secret = 'given-password'
token_url = 'https://myauthserver/tokens'

auth = HTTPBasicAuth(client_id, client_secret)
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, auth=auth)


secured_resource = 'https://my-secured-resource'

r = oauth.get(secured_resource)

print r.json()