# InfrastructureregionAutocompleteElementResponse

A Infrastructureregion AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_infrastructureregion_id** | **int** | The unique ID of the Infrastructureregion | 
**s_infrastructureregion_code** | **str** | The region code | 
**b_infrastructureregion_programmer** | **bool** | Whether Infrastructureregion is Programmer or not | 
**b_infrastructureregion_isactive** | **bool** | Whether the Infrastructureregion is active or not | 

## Example

```python
from eZmaxApi.models.infrastructureregion_autocomplete_element_response import InfrastructureregionAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureregionAutocompleteElementResponse from a JSON string
infrastructureregion_autocomplete_element_response_instance = InfrastructureregionAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(InfrastructureregionAutocompleteElementResponse.to_json())

# convert the object into a dict
infrastructureregion_autocomplete_element_response_dict = infrastructureregion_autocomplete_element_response_instance.to_dict()
# create an instance of InfrastructureregionAutocompleteElementResponse from a dict
infrastructureregion_autocomplete_element_response_from_dict = InfrastructureregionAutocompleteElementResponse.from_dict(infrastructureregion_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


