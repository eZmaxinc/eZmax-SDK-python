# EzsignsignatureGetObjectV4ResponseMPayload

Payload for GET /4/object/ezsignsignature/{pkiEzsignsignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignature** | [**EzsignsignatureResponseCompoundV3**](EzsignsignatureResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_object_v4_response_m_payload import EzsignsignatureGetObjectV4ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetObjectV4ResponseMPayload from a JSON string
ezsignsignature_get_object_v4_response_m_payload_instance = EzsignsignatureGetObjectV4ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureGetObjectV4ResponseMPayload.to_json())

# convert the object into a dict
ezsignsignature_get_object_v4_response_m_payload_dict = ezsignsignature_get_object_v4_response_m_payload_instance.to_dict()
# create an instance of EzsignsignatureGetObjectV4ResponseMPayload from a dict
ezsignsignature_get_object_v4_response_m_payload_from_dict = EzsignsignatureGetObjectV4ResponseMPayload.from_dict(ezsignsignature_get_object_v4_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


