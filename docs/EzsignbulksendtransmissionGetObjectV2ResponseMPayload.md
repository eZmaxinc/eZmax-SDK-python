# EzsignbulksendtransmissionGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksendtransmission** | [**EzsignbulksendtransmissionResponseCompound**](EzsignbulksendtransmissionResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_get_object_v2_response_m_payload import EzsignbulksendtransmissionGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionGetObjectV2ResponseMPayload from a JSON string
ezsignbulksendtransmission_get_object_v2_response_m_payload_instance = EzsignbulksendtransmissionGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendtransmissionGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsignbulksendtransmission_get_object_v2_response_m_payload_dict = ezsignbulksendtransmission_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendtransmissionGetObjectV2ResponseMPayload from a dict
ezsignbulksendtransmission_get_object_v2_response_m_payload_form_dict = ezsignbulksendtransmission_get_object_v2_response_m_payload.from_dict(ezsignbulksendtransmission_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


