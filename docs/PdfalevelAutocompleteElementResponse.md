# PdfalevelAutocompleteElementResponse

A Pdfalevel AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_pdfalevel_id** | **int** | The unique ID of the Pdfalevel | 
**s_pdfalevel_name** | **str** | The name of the Pdfalevel | 
**b_pdfalevel_isactive** | **bool** | Whether the Pdfalevel is active or not | 

## Example

```python
from eZmaxApi.models.pdfalevel_autocomplete_element_response import PdfalevelAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PdfalevelAutocompleteElementResponse from a JSON string
pdfalevel_autocomplete_element_response_instance = PdfalevelAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(PdfalevelAutocompleteElementResponse.to_json())

# convert the object into a dict
pdfalevel_autocomplete_element_response_dict = pdfalevel_autocomplete_element_response_instance.to_dict()
# create an instance of PdfalevelAutocompleteElementResponse from a dict
pdfalevel_autocomplete_element_response_from_dict = PdfalevelAutocompleteElementResponse.from_dict(pdfalevel_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


