# AuthenticationexternalCreateObjectV1Response

Response for POST /1/object/authenticationexternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AuthenticationexternalCreateObjectV1ResponseMPayload**](AuthenticationexternalCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_create_object_v1_response import AuthenticationexternalCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalCreateObjectV1Response from a JSON string
authenticationexternal_create_object_v1_response_instance = AuthenticationexternalCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalCreateObjectV1Response.to_json())

# convert the object into a dict
authenticationexternal_create_object_v1_response_dict = authenticationexternal_create_object_v1_response_instance.to_dict()
# create an instance of AuthenticationexternalCreateObjectV1Response from a dict
authenticationexternal_create_object_v1_response_from_dict = AuthenticationexternalCreateObjectV1Response.from_dict(authenticationexternal_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


