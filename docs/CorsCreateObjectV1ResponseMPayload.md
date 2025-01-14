# CorsCreateObjectV1ResponseMPayload

Payload for POST /1/object/cors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_cors_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.cors_create_object_v1_response_m_payload import CorsCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CorsCreateObjectV1ResponseMPayload from a JSON string
cors_create_object_v1_response_m_payload_instance = CorsCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CorsCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
cors_create_object_v1_response_m_payload_dict = cors_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of CorsCreateObjectV1ResponseMPayload from a dict
cors_create_object_v1_response_m_payload_from_dict = CorsCreateObjectV1ResponseMPayload.from_dict(cors_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


