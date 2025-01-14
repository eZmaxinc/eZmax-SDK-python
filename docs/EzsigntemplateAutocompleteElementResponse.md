# EzsigntemplateAutocompleteElementResponse

A Ezsigntemplate AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**b_ezsigntemplate_isactive** | **bool** | Whether the Ezsigntemplate is active or not | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_autocomplete_element_response import EzsigntemplateAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateAutocompleteElementResponse from a JSON string
ezsigntemplate_autocomplete_element_response_instance = EzsigntemplateAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateAutocompleteElementResponse.to_json())

# convert the object into a dict
ezsigntemplate_autocomplete_element_response_dict = ezsigntemplate_autocomplete_element_response_instance.to_dict()
# create an instance of EzsigntemplateAutocompleteElementResponse from a dict
ezsigntemplate_autocomplete_element_response_from_dict = EzsigntemplateAutocompleteElementResponse.from_dict(ezsigntemplate_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


