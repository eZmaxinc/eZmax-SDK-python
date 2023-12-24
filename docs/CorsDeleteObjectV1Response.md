# CorsDeleteObjectV1Response

Response for DELETE /1/object/cors/{pkiCorsID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.cors_delete_object_v1_response import CorsDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CorsDeleteObjectV1Response from a JSON string
cors_delete_object_v1_response_instance = CorsDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print CorsDeleteObjectV1Response.to_json()

# convert the object into a dict
cors_delete_object_v1_response_dict = cors_delete_object_v1_response_instance.to_dict()
# create an instance of CorsDeleteObjectV1Response from a dict
cors_delete_object_v1_response_form_dict = cors_delete_object_v1_response.from_dict(cors_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


