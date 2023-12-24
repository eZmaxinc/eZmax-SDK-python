# CorsCreateObjectV1Response

Response for POST /1/object/cors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CorsCreateObjectV1ResponseMPayload**](CorsCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.cors_create_object_v1_response import CorsCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CorsCreateObjectV1Response from a JSON string
cors_create_object_v1_response_instance = CorsCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print CorsCreateObjectV1Response.to_json()

# convert the object into a dict
cors_create_object_v1_response_dict = cors_create_object_v1_response_instance.to_dict()
# create an instance of CorsCreateObjectV1Response from a dict
cors_create_object_v1_response_form_dict = cors_create_object_v1_response.from_dict(cors_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


