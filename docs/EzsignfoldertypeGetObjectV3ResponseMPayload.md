# EzsignfoldertypeGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldertype** | [**EzsignfoldertypeResponseCompoundV3**](EzsignfoldertypeResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_get_object_v3_response_m_payload import EzsignfoldertypeGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeGetObjectV3ResponseMPayload from a JSON string
ezsignfoldertype_get_object_v3_response_m_payload_instance = EzsignfoldertypeGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsignfoldertype_get_object_v3_response_m_payload_dict = ezsignfoldertype_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldertypeGetObjectV3ResponseMPayload from a dict
ezsignfoldertype_get_object_v3_response_m_payload_form_dict = ezsignfoldertype_get_object_v3_response_m_payload.from_dict(ezsignfoldertype_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


