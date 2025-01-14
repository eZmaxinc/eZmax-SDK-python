# EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload

Payload for POST /2/object/ezsignbulksend/{pkiEzsignbulksendID}/createEzsignbulksendtransmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksendtransmission** | [**EzsignbulksendtransmissionResponse**](EzsignbulksendtransmissionResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload import EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload from a JSON string
ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload_instance = EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload_dict = ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload from a dict
ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload_from_dict = EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload.from_dict(ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


