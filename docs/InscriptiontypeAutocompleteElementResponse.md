# InscriptiontypeAutocompleteElementResponse

A Inscriptiontype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscriptiontype_id** | **int** | The unique ID of the Inscriptiontype | 
**s_inscriptiontype_name_x** | **str** | The name of the Inscriptiontype in the language of the requester | 

## Example

```python
from eZmaxApi.models.inscriptiontype_autocomplete_element_response import InscriptiontypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontypeAutocompleteElementResponse from a JSON string
inscriptiontype_autocomplete_element_response_instance = InscriptiontypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(InscriptiontypeAutocompleteElementResponse.to_json())

# convert the object into a dict
inscriptiontype_autocomplete_element_response_dict = inscriptiontype_autocomplete_element_response_instance.to_dict()
# create an instance of InscriptiontypeAutocompleteElementResponse from a dict
inscriptiontype_autocomplete_element_response_from_dict = InscriptiontypeAutocompleteElementResponse.from_dict(inscriptiontype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


