# CustomEzsignfoldersignerassociationActionableElementResponse

A Ezsignfoldersignerassociation Object with actionable elements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
print(CustomEzsignfoldersignerassociationActionableElementResponse.to_json())

# convert the object into a dict
custom_ezsignfoldersignerassociation_actionable_element_response_dict = custom_ezsignfoldersignerassociation_actionable_element_response_instance.to_dict()
# create an instance of CustomEzsignfoldersignerassociationActionableElementResponse from a dict
custom_ezsignfoldersignerassociation_actionable_element_response_from_dict = CustomEzsignfoldersignerassociationActionableElementResponse.from_dict(custom_ezsignfoldersignerassociation_actionable_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


