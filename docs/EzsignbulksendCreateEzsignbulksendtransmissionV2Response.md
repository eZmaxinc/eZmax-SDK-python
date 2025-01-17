# EzsignbulksendCreateEzsignbulksendtransmissionV2Response

Response for POST /2/object/ezsignbulksend/{pkiEzsignbulksendID}/createEzsignbulksendtransmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload**](EzsignbulksendCreateEzsignbulksendtransmissionV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v2_response import EzsignbulksendCreateEzsignbulksendtransmissionV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV2Response from a JSON string
ezsignbulksend_create_ezsignbulksendtransmission_v2_response_instance = EzsignbulksendCreateEzsignbulksendtransmissionV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendCreateEzsignbulksendtransmissionV2Response.to_json())

# convert the object into a dict
ezsignbulksend_create_ezsignbulksendtransmission_v2_response_dict = ezsignbulksend_create_ezsignbulksendtransmission_v2_response_instance.to_dict()
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV2Response from a dict
ezsignbulksend_create_ezsignbulksendtransmission_v2_response_from_dict = EzsignbulksendCreateEzsignbulksendtransmissionV2Response.from_dict(ezsignbulksend_create_ezsignbulksendtransmission_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


