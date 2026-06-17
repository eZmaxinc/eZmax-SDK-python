# EzsignfolderGetActionableElementsForSignerV1ResponseMPayload

Payload for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getActionableElementsForSigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureResponseCompound]**](EzsignsignatureResponseCompound.md) |  | 
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupResponseCompound]**](EzsignformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_actionable_elements_for_signer_v1_response_m_payload import EzsignfolderGetActionableElementsForSignerV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetActionableElementsForSignerV1ResponseMPayload from a JSON string
ezsignfolder_get_actionable_elements_for_signer_v1_response_m_payload_instance = EzsignfolderGetActionableElementsForSignerV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetActionableElementsForSignerV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_actionable_elements_for_signer_v1_response_m_payload_dict = ezsignfolder_get_actionable_elements_for_signer_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetActionableElementsForSignerV1ResponseMPayload from a dict
ezsignfolder_get_actionable_elements_for_signer_v1_response_m_payload_from_dict = EzsignfolderGetActionableElementsForSignerV1ResponseMPayload.from_dict(ezsignfolder_get_actionable_elements_for_signer_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


