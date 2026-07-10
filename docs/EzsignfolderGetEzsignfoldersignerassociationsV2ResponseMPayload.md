# EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload

Payload for GET /2/object/ezsignfolder/{pkiEzsignfolder}/getEzsignfoldersignerassociations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldersignerassociation** | [**List[CustomEzsignfoldersignerassociationActionableElementResponseV2]**](CustomEzsignfoldersignerassociationActionableElementResponseV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsignfoldersignerassociations_v2_response_m_payload import EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload from a JSON string
ezsignfolder_get_ezsignfoldersignerassociations_v2_response_m_payload_instance = EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_ezsignfoldersignerassociations_v2_response_m_payload_dict = ezsignfolder_get_ezsignfoldersignerassociations_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload from a dict
ezsignfolder_get_ezsignfoldersignerassociations_v2_response_m_payload_from_dict = EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload.from_dict(ezsignfolder_get_ezsignfoldersignerassociations_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


