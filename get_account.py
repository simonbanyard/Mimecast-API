import base64
import email.utils
import hashlib
import hmac
import json
import uuid

import requests

# Setup required variables
base_url = "https://eu-api.mimecast.com"
uri = "/api/account/get-account"
url = base_url + uri
access_key = "xxx"
secret_key = "xxx"
app_id = "xxx"
app_key = "xxx"

# Generate request header values
request_id = str(uuid.uuid4())
hdr_date = email.utils.formatdate(localtime=False)

# DataToSign is used in hmac_sha1
data_to_sign = f"{hdr_date}:{request_id}:{uri}:{app_key}"

# Create the HMAC SHA1 of the Base64 decoded secret key
# for the Authorization header
hmac_sha1 = hmac.new(base64.b64decode(secret_key), data_to_sign.encode(),
                     digestmod=hashlib.sha1).digest()

# Use the HMAC SHA1 value to sign the data_to_sign variable"
sig = base64.b64encode(hmac_sha1).rstrip()

# Generate auth
auth = f'MC {access_key}:{sig.decode()}'

# Create request headers
headers = {
    'Authorization': auth,
    'x-mc-app-id': app_id,
    'x-mc-date': hdr_date,
    'x-mc-req-id': request_id,
    'Content-Type': 'application/json'
}
payload = {'data': []}

# Make request
r = requests.post(url=url, data=str(payload), headers=headers)
response = json.loads(r.text)
if r.status_code == 200:
    print(f"Success: {r.status_code} - {r.reason}.")
    print(json.dumps(response['data'][0], indent=2))
else:
    print("Request failed.")
    print(f"Error: {r.status_code} - {r.reason}.")
    print(f"Reason: {response['fail'][0]['errors'][0]['message']}.")
