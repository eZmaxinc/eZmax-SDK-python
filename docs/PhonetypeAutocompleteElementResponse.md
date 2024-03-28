# PhonetypeAutocompleteElementResponse

A Phonetype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_phonetype_id** | **int** | The unique ID of the Phonetype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| |3|Mobile| |4|Fax| |5|Pager| |6|Toll Free| | 
**s_phonetype_name_x** | **str** | The name of the Phonetype in the language of the requester | 
**b_phonetype_isactive** | **bool** | Whether the Phonetype is active or not | 

## Example

```python
from eZmaxApi.models.phonetype_autocomplete_element_response import PhonetypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhonetypeAutocompleteElementResponse from a JSON string
phonetype_autocomplete_element_response_instance = PhonetypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(PhonetypeAutocompleteElementResponse.to_json())

# convert the object into a dict
phonetype_autocomplete_element_response_dict = phonetype_autocomplete_element_response_instance.to_dict()
# create an instance of PhonetypeAutocompleteElementResponse from a dict
phonetype_autocomplete_element_response_form_dict = phonetype_autocomplete_element_response.from_dict(phonetype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


