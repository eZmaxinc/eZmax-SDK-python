# EzsignsignatureCreateObjectV3Response

Response for POST /3/object/ezsignsignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignsignatureCreateObjectV3ResponseMPayload**](EzsignsignatureCreateObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_create_object_v3_response import EzsignsignatureCreateObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureCreateObjectV3Response from a JSON string
ezsignsignature_create_object_v3_response_instance = EzsignsignatureCreateObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureCreateObjectV3Response.to_json())

# convert the object into a dict
ezsignsignature_create_object_v3_response_dict = ezsignsignature_create_object_v3_response_instance.to_dict()
# create an instance of EzsignsignatureCreateObjectV3Response from a dict
ezsignsignature_create_object_v3_response_from_dict = EzsignsignatureCreateObjectV3Response.from_dict(ezsignsignature_create_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


