# EzsignfolderGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignfolder/{pkiEzsignfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfolder** | [**EzsignfolderResponseCompound**](EzsignfolderResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_object_v2_response_m_payload import EzsignfolderGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetObjectV2ResponseMPayload from a JSON string
ezsignfolder_get_object_v2_response_m_payload_instance = EzsignfolderGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_object_v2_response_m_payload_dict = ezsignfolder_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetObjectV2ResponseMPayload from a dict
ezsignfolder_get_object_v2_response_m_payload_form_dict = ezsignfolder_get_object_v2_response_m_payload.from_dict(ezsignfolder_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


