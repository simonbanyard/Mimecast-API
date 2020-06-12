import auth
import json
import requests

uri = "/api/user/get-profile"

r = requests.post(
    url=auth.base_url + uri,
    headers={"Authorization": auth.authentication(uri),
             "x-mc-app-id": auth.app_id,
             "x-mc-date": auth.hdr_date,
             "x-mc-req-id": auth.request_id,
             "Content-Type": "application/json"},
    data=str({"data": [{"emailAddress": "simon@banyard.org", "showAvatar":
        False}]})
)

mc_response = json.loads(r.content)
print(f"HTTP Response Body:\n{json.dumps(mc_response, indent=2)}")
