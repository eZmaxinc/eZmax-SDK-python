# AttachmentrejectreasonAutocompleteElementResponse

A Attachmentrejectreason AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_attachmentrejectreason_id** | **int** | The unique ID of the Attachmentrejectreason | 
**s_attachmentrejectreasonname_x** | **str** | The name of the Attachmentrejectreason in the language of the requester | 
**b_attachmentrejectreason_isactive** | **bool** | Whether the Attachmentrejectreason is active or not | 

## Example

```python
from eZmaxApi.models.attachmentrejectreason_autocomplete_element_response import AttachmentrejectreasonAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentrejectreasonAutocompleteElementResponse from a JSON string
attachmentrejectreason_autocomplete_element_response_instance = AttachmentrejectreasonAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(AttachmentrejectreasonAutocompleteElementResponse.to_json())

# convert the object into a dict
attachmentrejectreason_autocomplete_element_response_dict = attachmentrejectreason_autocomplete_element_response_instance.to_dict()
# create an instance of AttachmentrejectreasonAutocompleteElementResponse from a dict
attachmentrejectreason_autocomplete_element_response_from_dict = AttachmentrejectreasonAutocompleteElementResponse.from_dict(attachmentrejectreason_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


