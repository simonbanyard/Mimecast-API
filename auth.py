import base64
import hashlib
import hmac
import uuid
from datetime import datetime
from dateutil.tz import tzlocal

# Setup account details
# base_url: Replace xx with the region the account is hosted in, see
# https://www.mimecast.com/tech-connect/documentation/api-overview/global-base-urls/
# Keys are obtained from your Mimecast account, see
# https://community.mimecast.com/s/article/Managing-API-Applications-505230018
base_url = "https://xx-api.mimecast.com"
access_key = "Access Key"
secret_key = "Secret Key"
app_id = "Application ID"
app_key = "Application Key"

# Generate UUID based on RFC4122 and Date/Time based on RFC1123/2822
request_id = str(uuid.uuid4())
hdr_date = datetime.now(tzlocal()).strftime("%a, %d %b %Y %H:%M:%S %Z")


def authentication(uri):
    data_to_sign = f"{hdr_date}:{request_id}:{uri}:{app_key}"
    hmac_sha1 = hmac.new(base64.b64decode(secret_key),
                         data_to_sign.encode("utf-8"),
                         digestmod=hashlib.sha1).digest()
    authorization = str(base64.b64encode(hmac_sha1).rstrip().decode())

    return f"MC {access_key}:{authorization}"


if __name__ == '__main__':
    endpoint = input("Enter URI: ")
    print(f"Authorization: {authentication(endpoint)}")
