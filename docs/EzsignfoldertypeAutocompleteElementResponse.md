# EzsignfoldertypeAutocompleteElementResponse

A Ezsignfoldertype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**pki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**b_ezsignfoldertype_isactive** | **bool** | Whether the Ezsignfoldertype is active or not | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_autocomplete_element_response import EzsignfoldertypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeAutocompleteElementResponse from a JSON string
ezsignfoldertype_autocomplete_element_response_instance = EzsignfoldertypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeAutocompleteElementResponse.to_json())

# convert the object into a dict
ezsignfoldertype_autocomplete_element_response_dict = ezsignfoldertype_autocomplete_element_response_instance.to_dict()
# create an instance of EzsignfoldertypeAutocompleteElementResponse from a dict
ezsignfoldertype_autocomplete_element_response_from_dict = EzsignfoldertypeAutocompleteElementResponse.from_dict(ezsignfoldertype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


