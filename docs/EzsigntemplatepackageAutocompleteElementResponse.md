# EzsigntemplatepackageAutocompleteElementResponse

A Ezsigntemplatepackage AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**s_ezsigntemplatepackage_description** | **str** | The description of the Ezsigntemplatepackage | 
**pki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**b_ezsigntemplatepackage_isactive** | **bool** | Whether the Ezsigntemplatepackage is active or not | 
**b_disabled** | **bool** | Indicates if the element is disabled in the context | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_autocomplete_element_response import EzsigntemplatepackageAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageAutocompleteElementResponse from a JSON string
ezsigntemplatepackage_autocomplete_element_response_instance = EzsigntemplatepackageAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageAutocompleteElementResponse.to_json())

# convert the object into a dict
ezsigntemplatepackage_autocomplete_element_response_dict = ezsigntemplatepackage_autocomplete_element_response_instance.to_dict()
# create an instance of EzsigntemplatepackageAutocompleteElementResponse from a dict
ezsigntemplatepackage_autocomplete_element_response_form_dict = ezsigntemplatepackage_autocomplete_element_response.from_dict(ezsigntemplatepackage_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


