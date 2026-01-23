# RealestateassociationAutocompleteElementResponse

A Realestateassociation AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_realestateassociation_id** | **int** | The unique ID of the Realestateassociation | 
**s_realestateassociation_name_x** | **str** | The name of the Realestateassociation | 
**s_realestateassociation_acronym_x** | **str** | The Acronym of the Realestateassociation in the language of the requester | 
**b_realestateassociation_isactive** | **bool** | Whether the Realestateassociation is active or not | 

## Example

```python
from eZmaxApi.models.realestateassociation_autocomplete_element_response import RealestateassociationAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RealestateassociationAutocompleteElementResponse from a JSON string
realestateassociation_autocomplete_element_response_instance = RealestateassociationAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(RealestateassociationAutocompleteElementResponse.to_json())

# convert the object into a dict
realestateassociation_autocomplete_element_response_dict = realestateassociation_autocomplete_element_response_instance.to_dict()
# create an instance of RealestateassociationAutocompleteElementResponse from a dict
realestateassociation_autocomplete_element_response_from_dict = RealestateassociationAutocompleteElementResponse.from_dict(realestateassociation_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


