# CorsGetObjectV2ResponseMPayload

Payload for GET /2/object/cors/{pkiCorsID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_cors** | [**CorsResponseCompound**](CorsResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.cors_get_object_v2_response_m_payload import CorsGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CorsGetObjectV2ResponseMPayload from a JSON string
cors_get_object_v2_response_m_payload_instance = CorsGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CorsGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
cors_get_object_v2_response_m_payload_dict = cors_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of CorsGetObjectV2ResponseMPayload from a dict
cors_get_object_v2_response_m_payload_from_dict = CorsGetObjectV2ResponseMPayload.from_dict(cors_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


