# EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload

Payload for GET /1/object/ezsignfolder/{pkiEzsignfolder}/getEzsignfoldersignerassociations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldersignerassociation** | [**List[CustomEzsignfoldersignerassociationActionableElementResponse]**](CustomEzsignfoldersignerassociationActionableElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload import EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload from a JSON string
ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload_instance = EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload_dict = ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload from a dict
ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload_form_dict = ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload.from_dict(ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


