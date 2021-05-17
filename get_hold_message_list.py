import auth
import datetime
import json
import requests

uri = "/api/provisioning/get-packages"
start_date =
end_date = datetime.

r = requests.post(
    url=auth.base_url + uri,
    headers={"Authorization": auth.authentication(uri),
             "x-mc-app-id": auth.app_id,
             "x-mc-date": auth.hdr_date,
             "x-mc-req-id": auth.request_id,
             "Content-Type": "application/json"},
    data=str({
    "data": [
        {
            "admin": "true",
            "start": "2015-11-16T14:49:18+0000",
            "searchBy": [
                {
                    "fieldName": "String",
                    "value": "String"
                }
            ],
            "end": "2015-11-16T14:49:18+0000",
            "filterBy": [
                {
                    "fieldName": "String",
                    "value": "String"
                }
            ]
        }
    ]
})
)

mc_response = json.loads(r.content)
print(f"HTTP Response Body:\n{json.dumps(mc_response, indent=2)}")