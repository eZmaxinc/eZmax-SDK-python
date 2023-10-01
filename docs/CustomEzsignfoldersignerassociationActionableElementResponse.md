# CustomEzsignfoldersignerassociationActionableElementResponse

A Ezsignfoldersignerassociation Object with actionable elements

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**b_ezsignfoldersignerassociation_delayedsend** | **bool** | If this flag is true the signatory is part of a delayed send. | 
**b_ezsignfoldersignerassociation_receivecopy** | **bool** | If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain&#39;t required to sign the document. | 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | 
**obj_ezsignsignergroup** | [**EzsignsignergroupResponseCompound**](EzsignsignergroupResponseCompound.md) |  | [optional] 
**obj_user** | [**EzsignfoldersignerassociationResponseCompoundUser**](EzsignfoldersignerassociationResponseCompoundUser.md) |  | [optional] 
**obj_ezsignsigner** | [**EzsignsignerResponseCompound**](EzsignsignerResponseCompound.md) |  | [optional] 
**b_ezsignfoldersignerassociation_hasactionableelements_current** | **bool** | Indicates if the Ezsignfoldersignerassociation has actionable elements in the current step | 
**b_ezsignfoldersignerassociation_hasactionableelements_future** | **bool** | Indicates if the Ezsignfoldersignerassociation has actionable elements in a future step | 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldersignerassociation_actionable_element_response import CustomEzsignfoldersignerassociationActionableElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldersignerassociationActionableElementResponse from a JSON string
custom_ezsignfoldersignerassociation_actionable_element_response_instance = CustomEzsignfoldersignerassociationActionableElementResponse.from_json(json)
# print the JSON string representation of the object
print CustomEzsignfoldersignerassociationActionableElementResponse.to_json()

# convert the object into a dict
custom_ezsignfoldersignerassociation_actionable_element_response_dict = custom_ezsignfoldersignerassociation_actionable_element_response_instance.to_dict()
# create an instance of CustomEzsignfoldersignerassociationActionableElementResponse from a dict
custom_ezsignfoldersignerassociation_actionable_element_response_form_dict = custom_ezsignfoldersignerassociation_actionable_element_response.from_dict(custom_ezsignfoldersignerassociation_actionable_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


