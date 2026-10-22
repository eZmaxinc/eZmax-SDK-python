# DocumenttypeAutocompleteElementResponse

A Documenttype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttype_id** | **int** | The unique ID of the Documenttype | 
**s_documenttype_name_x** | **str** | The name of the Documenttype in the language of the requester | 
**b_documenttype_isactive** | **bool** | Whether the documenttype is active or not | 

## Example

```python
from eZmaxApi.models.documenttype_autocomplete_element_response import DocumenttypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeAutocompleteElementResponse from a JSON string
documenttype_autocomplete_element_response_instance = DocumenttypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeAutocompleteElementResponse.to_json())

# convert the object into a dict
documenttype_autocomplete_element_response_dict = documenttype_autocomplete_element_response_instance.to_dict()
# create an instance of DocumenttypeAutocompleteElementResponse from a dict
documenttype_autocomplete_element_response_from_dict = DocumenttypeAutocompleteElementResponse.from_dict(documenttype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


