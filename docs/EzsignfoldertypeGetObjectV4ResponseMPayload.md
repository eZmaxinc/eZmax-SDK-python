# EzsignfoldertypeGetObjectV4ResponseMPayload

Payload for GET /4/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldertype** | [**EzsignfoldertypeResponseCompoundV4**](EzsignfoldertypeResponseCompoundV4.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_get_object_v4_response_m_payload import EzsignfoldertypeGetObjectV4ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeGetObjectV4ResponseMPayload from a JSON string
ezsignfoldertype_get_object_v4_response_m_payload_instance = EzsignfoldertypeGetObjectV4ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeGetObjectV4ResponseMPayload.to_json())

# convert the object into a dict
ezsignfoldertype_get_object_v4_response_m_payload_dict = ezsignfoldertype_get_object_v4_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldertypeGetObjectV4ResponseMPayload from a dict
ezsignfoldertype_get_object_v4_response_m_payload_from_dict = EzsignfoldertypeGetObjectV4ResponseMPayload.from_dict(ezsignfoldertype_get_object_v4_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


