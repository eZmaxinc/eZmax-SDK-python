# EzsignfoldersignerassociationRequestCompound

An Ezsignfoldersignerassociation Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_ezsignsignergroup_id** | **int** | The unique ID of the Ezsignsignergroup | [optional] 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**b_ezsignfoldersignerassociation_receivecopy** | **bool** | If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain&#39;t required to sign the document. | [optional] 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | [optional] 
**obj_ezsignsigner** | [**EzsignsignerRequestCompound**](EzsignsignerRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_request_compound import EzsignfoldersignerassociationRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationRequestCompound from a JSON string
ezsignfoldersignerassociation_request_compound_instance = EzsignfoldersignerassociationRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationRequestCompound.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_request_compound_dict = ezsignfoldersignerassociation_request_compound_instance.to_dict()
# create an instance of EzsignfoldersignerassociationRequestCompound from a dict
ezsignfoldersignerassociation_request_compound_from_dict = EzsignfoldersignerassociationRequestCompound.from_dict(ezsignfoldersignerassociation_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


