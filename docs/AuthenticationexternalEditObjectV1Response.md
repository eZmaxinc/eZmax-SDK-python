# AuthenticationexternalEditObjectV1Response

Response for PUT /1/object/authenticationexternal/{pkiAuthenticationexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.authenticationexternal_edit_object_v1_response import AuthenticationexternalEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalEditObjectV1Response from a JSON string
authenticationexternal_edit_object_v1_response_instance = AuthenticationexternalEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalEditObjectV1Response.to_json())

# convert the object into a dict
authenticationexternal_edit_object_v1_response_dict = authenticationexternal_edit_object_v1_response_instance.to_dict()
# create an instance of AuthenticationexternalEditObjectV1Response from a dict
authenticationexternal_edit_object_v1_response_from_dict = AuthenticationexternalEditObjectV1Response.from_dict(authenticationexternal_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


