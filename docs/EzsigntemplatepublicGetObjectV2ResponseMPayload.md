# EzsigntemplatepublicGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepublic** | [**EzsigntemplatepublicResponseCompound**](EzsigntemplatepublicResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_object_v2_response_m_payload import EzsigntemplatepublicGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetObjectV2ResponseMPayload from a JSON string
ezsigntemplatepublic_get_object_v2_response_m_payload_instance = EzsigntemplatepublicGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_object_v2_response_m_payload_dict = ezsigntemplatepublic_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepublicGetObjectV2ResponseMPayload from a dict
ezsigntemplatepublic_get_object_v2_response_m_payload_from_dict = EzsigntemplatepublicGetObjectV2ResponseMPayload.from_dict(ezsigntemplatepublic_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


