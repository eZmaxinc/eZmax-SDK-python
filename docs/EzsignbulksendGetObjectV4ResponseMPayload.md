# EzsignbulksendGetObjectV4ResponseMPayload

Payload for GET /4/object/ezsignbulksend/{pkiEzsignbulksendID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksend** | [**EzsignbulksendResponseCompoundV4**](EzsignbulksendResponseCompoundV4.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_object_v4_response_m_payload import EzsignbulksendGetObjectV4ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetObjectV4ResponseMPayload from a JSON string
ezsignbulksend_get_object_v4_response_m_payload_instance = EzsignbulksendGetObjectV4ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendGetObjectV4ResponseMPayload.to_json())

# convert the object into a dict
ezsignbulksend_get_object_v4_response_m_payload_dict = ezsignbulksend_get_object_v4_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendGetObjectV4ResponseMPayload from a dict
ezsignbulksend_get_object_v4_response_m_payload_from_dict = EzsignbulksendGetObjectV4ResponseMPayload.from_dict(ezsignbulksend_get_object_v4_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


