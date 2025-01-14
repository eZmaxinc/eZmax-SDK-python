# AuthenticationexternalEditObjectV1Request

Request for PUT /1/object/authenticationexternal/{pkiAuthenticationexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_authenticationexternal** | [**AuthenticationexternalRequestCompound**](AuthenticationexternalRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_edit_object_v1_request import AuthenticationexternalEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalEditObjectV1Request from a JSON string
authenticationexternal_edit_object_v1_request_instance = AuthenticationexternalEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalEditObjectV1Request.to_json())

# convert the object into a dict
authenticationexternal_edit_object_v1_request_dict = authenticationexternal_edit_object_v1_request_instance.to_dict()
# create an instance of AuthenticationexternalEditObjectV1Request from a dict
authenticationexternal_edit_object_v1_request_from_dict = AuthenticationexternalEditObjectV1Request.from_dict(authenticationexternal_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


