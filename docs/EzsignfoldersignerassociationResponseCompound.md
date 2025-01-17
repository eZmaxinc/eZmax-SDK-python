# EzsignfoldersignerassociationResponseCompound

An Ezsignfoldersignerassociation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignergroup** | [**EzsignsignergroupResponseCompound**](EzsignsignergroupResponseCompound.md) |  | [optional] 
**obj_user** | [**EzsignfoldersignerassociationResponseCompoundUser**](EzsignfoldersignerassociationResponseCompoundUser.md) |  | [optional] 
**obj_ezsignsigner** | [**EzsignsignerResponseCompound**](EzsignsignerResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_response_compound import EzsignfoldersignerassociationResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationResponseCompound from a JSON string
ezsignfoldersignerassociation_response_compound_instance = EzsignfoldersignerassociationResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationResponseCompound.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_response_compound_dict = ezsignfoldersignerassociation_response_compound_instance.to_dict()
# create an instance of EzsignfoldersignerassociationResponseCompound from a dict
ezsignfoldersignerassociation_response_compound_from_dict = EzsignfoldersignerassociationResponseCompound.from_dict(ezsignfoldersignerassociation_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


