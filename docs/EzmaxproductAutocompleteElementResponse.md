# EzmaxproductAutocompleteElementResponse

A Ezmaxproduct AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxproduct_id** | **int** | The unique ID of the Ezmaxproduct | 
**s_ezmaxproduct_description_x** | **str** | The description of the Ezmaxproduct in the language of the requester | 
**b_ezmaxproduct_isactive** | **bool** | Whether the Ezmaxproduct is active or not | 

## Example

```python
from eZmaxApi.models.ezmaxproduct_autocomplete_element_response import EzmaxproductAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxproductAutocompleteElementResponse from a JSON string
ezmaxproduct_autocomplete_element_response_instance = EzmaxproductAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxproductAutocompleteElementResponse.to_json())

# convert the object into a dict
ezmaxproduct_autocomplete_element_response_dict = ezmaxproduct_autocomplete_element_response_instance.to_dict()
# create an instance of EzmaxproductAutocompleteElementResponse from a dict
ezmaxproduct_autocomplete_element_response_from_dict = EzmaxproductAutocompleteElementResponse.from_dict(ezmaxproduct_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


