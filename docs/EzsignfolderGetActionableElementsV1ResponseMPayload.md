# EzsignfolderGetActionableElementsV1ResponseMPayload

Payload for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getActionableElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureResponseCompound]**](EzsignsignatureResponseCompound.md) |  | 
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupResponseCompound]**](EzsignformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_actionable_elements_v1_response_m_payload import EzsignfolderGetActionableElementsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetActionableElementsV1ResponseMPayload from a JSON string
ezsignfolder_get_actionable_elements_v1_response_m_payload_instance = EzsignfolderGetActionableElementsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetActionableElementsV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_actionable_elements_v1_response_m_payload_dict = ezsignfolder_get_actionable_elements_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetActionableElementsV1ResponseMPayload from a dict
ezsignfolder_get_actionable_elements_v1_response_m_payload_form_dict = ezsignfolder_get_actionable_elements_v1_response_m_payload.from_dict(ezsignfolder_get_actionable_elements_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


