# EzmaxinvoicingAutocompleteElementResponse

A Ezmaxinvoicing AutocompleteElement Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yyyymm_ezmaxinvoicing** | **str** | The YYYYMM period of the Ezmaxinvoicing | 
**pki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | 
**b_ezmaxinvoicing_isactive** | **bool** | Whether the Ezmaxinvoicing is active or not | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicing_autocomplete_element_response import EzmaxinvoicingAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingAutocompleteElementResponse from a JSON string
ezmaxinvoicing_autocomplete_element_response_instance = EzmaxinvoicingAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print EzmaxinvoicingAutocompleteElementResponse.to_json()

# convert the object into a dict
ezmaxinvoicing_autocomplete_element_response_dict = ezmaxinvoicing_autocomplete_element_response_instance.to_dict()
# create an instance of EzmaxinvoicingAutocompleteElementResponse from a dict
ezmaxinvoicing_autocomplete_element_response_form_dict = ezmaxinvoicing_autocomplete_element_response.from_dict(ezmaxinvoicing_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


