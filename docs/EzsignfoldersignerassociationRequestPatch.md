# EzsignfoldersignerassociationRequestPatch

An Ezsignfoldersignerassociation Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_request_patch import EzsignfoldersignerassociationRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationRequestPatch from a JSON string
ezsignfoldersignerassociation_request_patch_instance = EzsignfoldersignerassociationRequestPatch.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationRequestPatch.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_request_patch_dict = ezsignfoldersignerassociation_request_patch_instance.to_dict()
# create an instance of EzsignfoldersignerassociationRequestPatch from a dict
ezsignfoldersignerassociation_request_patch_form_dict = ezsignfoldersignerassociation_request_patch.from_dict(ezsignfoldersignerassociation_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


