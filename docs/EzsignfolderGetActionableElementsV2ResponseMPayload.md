# EzsignfolderGetActionableElementsV2ResponseMPayload

Payload for GET /2/object/ezsignfolder/{pkiEzsignfolderID}/getActionableElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureResponseCompound]**](EzsignsignatureResponseCompound.md) |  | 
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupResponseCompound]**](EzsignformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_actionable_elements_v2_response_m_payload import EzsignfolderGetActionableElementsV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetActionableElementsV2ResponseMPayload from a JSON string
ezsignfolder_get_actionable_elements_v2_response_m_payload_instance = EzsignfolderGetActionableElementsV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetActionableElementsV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_actionable_elements_v2_response_m_payload_dict = ezsignfolder_get_actionable_elements_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetActionableElementsV2ResponseMPayload from a dict
ezsignfolder_get_actionable_elements_v2_response_m_payload_from_dict = EzsignfolderGetActionableElementsV2ResponseMPayload.from_dict(ezsignfolder_get_actionable_elements_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


