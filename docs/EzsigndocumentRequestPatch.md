# EzsigndocumentRequestPatch

An Ezsigndocument Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | [optional] 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_request_patch import EzsigndocumentRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentRequestPatch from a JSON string
ezsigndocument_request_patch_instance = EzsigndocumentRequestPatch.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentRequestPatch.to_json())

# convert the object into a dict
ezsigndocument_request_patch_dict = ezsigndocument_request_patch_instance.to_dict()
# create an instance of EzsigndocumentRequestPatch from a dict
ezsigndocument_request_patch_form_dict = ezsigndocument_request_patch.from_dict(ezsigndocument_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


