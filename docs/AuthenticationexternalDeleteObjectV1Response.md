# AuthenticationexternalDeleteObjectV1Response

Response for DELETE /1/object/authenticationexternal/{pkiAuthenticationexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.authenticationexternal_delete_object_v1_response import AuthenticationexternalDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalDeleteObjectV1Response from a JSON string
authenticationexternal_delete_object_v1_response_instance = AuthenticationexternalDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalDeleteObjectV1Response.to_json())

# convert the object into a dict
authenticationexternal_delete_object_v1_response_dict = authenticationexternal_delete_object_v1_response_instance.to_dict()
# create an instance of AuthenticationexternalDeleteObjectV1Response from a dict
authenticationexternal_delete_object_v1_response_from_dict = AuthenticationexternalDeleteObjectV1Response.from_dict(authenticationexternal_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


