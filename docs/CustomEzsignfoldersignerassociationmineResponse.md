# CustomEzsignfoldersignerassociationmineResponse

A custom Ezsignfoldersignerassociation Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldersignerassociationmine_response import CustomEzsignfoldersignerassociationmineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldersignerassociationmineResponse from a JSON string
custom_ezsignfoldersignerassociationmine_response_instance = CustomEzsignfoldersignerassociationmineResponse.from_json(json)
# print the JSON string representation of the object
print CustomEzsignfoldersignerassociationmineResponse.to_json()

# convert the object into a dict
custom_ezsignfoldersignerassociationmine_response_dict = custom_ezsignfoldersignerassociationmine_response_instance.to_dict()
# create an instance of CustomEzsignfoldersignerassociationmineResponse from a dict
custom_ezsignfoldersignerassociationmine_response_form_dict = custom_ezsignfoldersignerassociationmine_response.from_dict(custom_ezsignfoldersignerassociationmine_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


