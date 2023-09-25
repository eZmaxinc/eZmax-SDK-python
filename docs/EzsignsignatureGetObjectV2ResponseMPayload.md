# EzsignsignatureGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignsignature/{pkiEzsignsignatureID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignature** | [**EzsignsignatureResponseCompound**](EzsignsignatureResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_object_v2_response_m_payload import EzsignsignatureGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetObjectV2ResponseMPayload from a JSON string
ezsignsignature_get_object_v2_response_m_payload_instance = EzsignsignatureGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignsignatureGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsignsignature_get_object_v2_response_m_payload_dict = ezsignsignature_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignsignatureGetObjectV2ResponseMPayload from a dict
ezsignsignature_get_object_v2_response_m_payload_form_dict = ezsignsignature_get_object_v2_response_m_payload.from_dict(ezsignsignature_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


