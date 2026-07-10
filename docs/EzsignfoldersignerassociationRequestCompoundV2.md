# EzsignfoldersignerassociationRequestCompoundV2

An Ezsignfoldersignerassociation Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_ezsignsignergroup_id** | **int** | The unique ID of the Ezsignsignergroup | [optional] 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**e_ezsignfoldersignerassociation_role** | [**FieldEEzsignfoldersignerassociationRole**](FieldEEzsignfoldersignerassociationRole.md) |  | 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | [optional] 
**obj_ezsignsigner** | [**EzsignsignerRequestCompound**](EzsignsignerRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_request_compound_v2 import EzsignfoldersignerassociationRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationRequestCompoundV2 from a JSON string
ezsignfoldersignerassociation_request_compound_v2_instance = EzsignfoldersignerassociationRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationRequestCompoundV2.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_request_compound_v2_dict = ezsignfoldersignerassociation_request_compound_v2_instance.to_dict()
# create an instance of EzsignfoldersignerassociationRequestCompoundV2 from a dict
ezsignfoldersignerassociation_request_compound_v2_from_dict = EzsignfoldersignerassociationRequestCompoundV2.from_dict(ezsignfoldersignerassociation_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


