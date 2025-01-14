# EzsignfoldersignerassociationGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**b_ezsignfoldersignerassociation_delayedsend** | **bool** | If this flag is true the signatory is part of a delayed send. | 
**b_ezsignfoldersignerassociation_receivecopy** | **bool** | If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain&#39;t required to sign the document. | 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | 
**b_ezsignfoldersignerassociation_allowsigninginperson** | **bool** | If the Ezsignfoldersignerassociation is allowed to sign in person or not | 
**obj_ezsignsignergroup** | [**EzsignsignergroupResponseCompound**](EzsignsignergroupResponseCompound.md) |  | [optional] 
**obj_user** | [**EzsignfoldersignerassociationResponseCompoundUser**](EzsignfoldersignerassociationResponseCompoundUser.md) |  | [optional] 
**obj_ezsignsigner** | [**EzsignsignerResponseCompound**](EzsignsignerResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_get_object_v1_response_m_payload import EzsignfoldersignerassociationGetObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationGetObjectV1ResponseMPayload from a JSON string
ezsignfoldersignerassociation_get_object_v1_response_m_payload_instance = EzsignfoldersignerassociationGetObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationGetObjectV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_get_object_v1_response_m_payload_dict = ezsignfoldersignerassociation_get_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldersignerassociationGetObjectV1ResponseMPayload from a dict
ezsignfoldersignerassociation_get_object_v1_response_m_payload_from_dict = EzsignfoldersignerassociationGetObjectV1ResponseMPayload.from_dict(ezsignfoldersignerassociation_get_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


