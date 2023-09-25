# BrandingAutocompleteElementResponse

Branding AutocompleteElement Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_branding_description_x** | **str** | The Description of the Branding in the language of the requester | 
**pki_branding_id** | **int** | The unique ID of the Branding | 
**b_branding_isactive** | **bool** | Whether the Branding is active or not | 

## Example

```python
from eZmaxApi.models.branding_autocomplete_element_response import BrandingAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingAutocompleteElementResponse from a JSON string
branding_autocomplete_element_response_instance = BrandingAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print BrandingAutocompleteElementResponse.to_json()

# convert the object into a dict
branding_autocomplete_element_response_dict = branding_autocomplete_element_response_instance.to_dict()
# create an instance of BrandingAutocompleteElementResponse from a dict
branding_autocomplete_element_response_form_dict = branding_autocomplete_element_response.from_dict(branding_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


