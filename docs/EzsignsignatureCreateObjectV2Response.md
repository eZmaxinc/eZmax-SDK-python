# EzsignsignatureCreateObjectV2Response

Response for POST /2/object/ezsignsignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignsignatureCreateObjectV2ResponseMPayload**](EzsignsignatureCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_create_object_v2_response import EzsignsignatureCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureCreateObjectV2Response from a JSON string
ezsignsignature_create_object_v2_response_instance = EzsignsignatureCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureCreateObjectV2Response.to_json())

# convert the object into a dict
ezsignsignature_create_object_v2_response_dict = ezsignsignature_create_object_v2_response_instance.to_dict()
# create an instance of EzsignsignatureCreateObjectV2Response from a dict
ezsignsignature_create_object_v2_response_from_dict = EzsignsignatureCreateObjectV2Response.from_dict(ezsignsignature_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


