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
access_key = ("mYtOL3XZCOwG96BOiFTZRuiS6gUCSg9ltXQQBuw9DU3YxzDQWq5_ptA9jdlBBO"
              "_TWIoSXDTu_Bn1HRu1neJ9GlsYiwjTY3hzCus8chW82AhF1Pptw4F8wbrPZCHJO"
              "QbZJIvmxpg0JaSiG8faa60wHg")
secret_key = ("hikaj5QQMkBc+KLc7veuoXortne0SiPB5kCffSeWaStOqYx"
              "+zJQJspVJKDumaEQsVx4d1+6hiIWEi1Bh5LzHKw== ")
app_id = "4ea70b79-69f5-4af1-a5b7-bc02db01e665"
app_key = "e05ae721-d485-4b28-8b32-293c1cc242a0"

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
