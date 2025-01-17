# EzsignsignatureGetObjectV3Response

Response for GET /3/object/ezsignsignature/{pkiEzsignsignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignsignatureGetObjectV3ResponseMPayload**](EzsignsignatureGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_object_v3_response import EzsignsignatureGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetObjectV3Response from a JSON string
ezsignsignature_get_object_v3_response_instance = EzsignsignatureGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureGetObjectV3Response.to_json())

# convert the object into a dict
ezsignsignature_get_object_v3_response_dict = ezsignsignature_get_object_v3_response_instance.to_dict()
# create an instance of EzsignsignatureGetObjectV3Response from a dict
ezsignsignature_get_object_v3_response_from_dict = EzsignsignatureGetObjectV3Response.from_dict(ezsignsignature_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


