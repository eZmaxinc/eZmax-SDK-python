# UserImpersonateV1Request

Request for POST /1/object/user/{pkiUserID}/impersonate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id** | **int** | The unique ID of the User | 
**i_expiration_minutes** | **int** | The number of minute before key is no longer active | 

## Example

```python
from eZmaxApi.models.user_impersonate_v1_request import UserImpersonateV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserImpersonateV1Request from a JSON string
user_impersonate_v1_request_instance = UserImpersonateV1Request.from_json(json)
# print the JSON string representation of the object
print(UserImpersonateV1Request.to_json())

# convert the object into a dict
user_impersonate_v1_request_dict = user_impersonate_v1_request_instance.to_dict()
# create an instance of UserImpersonateV1Request from a dict
user_impersonate_v1_request_from_dict = UserImpersonateV1Request.from_dict(user_impersonate_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


