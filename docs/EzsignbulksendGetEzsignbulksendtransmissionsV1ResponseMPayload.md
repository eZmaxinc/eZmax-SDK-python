# EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload

Payload for GET /1/object/ezsignbulksend/{pkiEzsignbulksend}/getEzsignbulksendtransmissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignbulksendtransmission** | [**List[EzsignbulksendtransmissionResponseCompound]**](EzsignbulksendtransmissionResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload import EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload from a JSON string
ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload_instance = EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload_dict = ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload from a dict
ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload_form_dict = ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload.from_dict(ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


