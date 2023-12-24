# CorsGetObjectV2Response

Response for GET /2/object/cors/{pkiCorsID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CorsGetObjectV2ResponseMPayload**](CorsGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.cors_get_object_v2_response import CorsGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CorsGetObjectV2Response from a JSON string
cors_get_object_v2_response_instance = CorsGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print CorsGetObjectV2Response.to_json()

# convert the object into a dict
cors_get_object_v2_response_dict = cors_get_object_v2_response_instance.to_dict()
# create an instance of CorsGetObjectV2Response from a dict
cors_get_object_v2_response_form_dict = cors_get_object_v2_response.from_dict(cors_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


