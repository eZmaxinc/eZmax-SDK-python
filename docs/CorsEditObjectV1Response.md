# CorsEditObjectV1Response

Response for PUT /1/object/cors/{pkiCorsID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.cors_edit_object_v1_response import CorsEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CorsEditObjectV1Response from a JSON string
cors_edit_object_v1_response_instance = CorsEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(CorsEditObjectV1Response.to_json())

# convert the object into a dict
cors_edit_object_v1_response_dict = cors_edit_object_v1_response_instance.to_dict()
# create an instance of CorsEditObjectV1Response from a dict
cors_edit_object_v1_response_from_dict = CorsEditObjectV1Response.from_dict(cors_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


