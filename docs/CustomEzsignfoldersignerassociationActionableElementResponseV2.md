# CustomEzsignfoldersignerassociationActionableElementResponseV2

A Ezsignfoldersignerassociation Object with actionable elements

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
**b_ezsignfoldersignerassociation_hasactionableelements_current** | **bool** | Indicates if the Ezsignfoldersignerassociation has actionable elements in the current step | 
**b_ezsignfoldersignerassociation_hasactionableelements_future** | **bool** | Indicates if the Ezsignfoldersignerassociation has actionable elements in a future step | 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldersignerassociation_actionable_element_response_v2 import CustomEzsignfoldersignerassociationActionableElementResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldersignerassociationActionableElementResponseV2 from a JSON string
custom_ezsignfoldersignerassociation_actionable_element_response_v2_instance = CustomEzsignfoldersignerassociationActionableElementResponseV2.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignfoldersignerassociationActionableElementResponseV2.to_json())

# convert the object into a dict
custom_ezsignfoldersignerassociation_actionable_element_response_v2_dict = custom_ezsignfoldersignerassociation_actionable_element_response_v2_instance.to_dict()
# create an instance of CustomEzsignfoldersignerassociationActionableElementResponseV2 from a dict
custom_ezsignfoldersignerassociation_actionable_element_response_v2_from_dict = CustomEzsignfoldersignerassociationActionableElementResponseV2.from_dict(custom_ezsignfoldersignerassociation_actionable_element_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


