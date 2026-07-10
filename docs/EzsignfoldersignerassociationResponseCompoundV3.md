# EzsignfoldersignerassociationResponseCompoundV3

An Ezsignfoldersignerassociation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**b_ezsignfoldersignerassociation_delayedsend** | **bool** | If this flag is true the signatory is part of a delayed send. | 
**e_ezsignfoldersignerassociation_role** | [**FieldEEzsignfoldersignerassociationRole**](FieldEEzsignfoldersignerassociationRole.md) |  | 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | 
**b_ezsignfoldersignerassociation_allowsigninginperson** | **bool** | If the Ezsignfoldersignerassociation is allowed to sign in person or not | 
**obj_ezsignsignergroup** | [**EzsignsignergroupResponseCompound**](EzsignsignergroupResponseCompound.md) |  | [optional] 
**obj_user** | [**EzsignfoldersignerassociationResponseCompoundUser**](EzsignfoldersignerassociationResponseCompoundUser.md) |  | [optional] 
**obj_ezsignsigner** | [**EzsignsignerResponseCompound**](EzsignsignerResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_response_compound_v3 import EzsignfoldersignerassociationResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationResponseCompoundV3 from a JSON string
ezsignfoldersignerassociation_response_compound_v3_instance = EzsignfoldersignerassociationResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationResponseCompoundV3.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_response_compound_v3_dict = ezsignfoldersignerassociation_response_compound_v3_instance.to_dict()
# create an instance of EzsignfoldersignerassociationResponseCompoundV3 from a dict
ezsignfoldersignerassociation_response_compound_v3_from_dict = EzsignfoldersignerassociationResponseCompoundV3.from_dict(ezsignfoldersignerassociation_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


