# InscriptionchecklistAutocompleteElementResponse

A Inscriptionchecklist AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscriptionchecklist_id** | **int** | The unique ID of the Inscriptionchecklist | 
**s_inscriptionchecklistelement_name_x** | **str** | The name of the Inscriptionchecklistelement in the language of the requester | 
**b_inscriptionchecklist_isactive** | **bool** | Whether the Inscriptionchecklist is active or not | 

## Example

```python
from eZmaxApi.models.inscriptionchecklist_autocomplete_element_response import InscriptionchecklistAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionchecklistAutocompleteElementResponse from a JSON string
inscriptionchecklist_autocomplete_element_response_instance = InscriptionchecklistAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(InscriptionchecklistAutocompleteElementResponse.to_json())

# convert the object into a dict
inscriptionchecklist_autocomplete_element_response_dict = inscriptionchecklist_autocomplete_element_response_instance.to_dict()
# create an instance of InscriptionchecklistAutocompleteElementResponse from a dict
inscriptionchecklist_autocomplete_element_response_from_dict = InscriptionchecklistAutocompleteElementResponse.from_dict(inscriptionchecklist_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


