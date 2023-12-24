# EzsignbulksendGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignbulksend/{pkiEzsignbulksendID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksend** | [**EzsignbulksendResponseCompound**](EzsignbulksendResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_object_v2_response_m_payload import EzsignbulksendGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetObjectV2ResponseMPayload from a JSON string
ezsignbulksend_get_object_v2_response_m_payload_instance = EzsignbulksendGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsignbulksend_get_object_v2_response_m_payload_dict = ezsignbulksend_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendGetObjectV2ResponseMPayload from a dict
ezsignbulksend_get_object_v2_response_m_payload_form_dict = ezsignbulksend_get_object_v2_response_m_payload.from_dict(ezsignbulksend_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


