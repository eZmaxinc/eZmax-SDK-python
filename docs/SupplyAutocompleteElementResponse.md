# SupplyAutocompleteElementResponse

A Supply AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_supply_id** | **int** | The unique ID of the Supply | 
**s_supply_description_x** | **str** | The description of the Supply in the language of the requester | 
**b_supply_isactive** | **bool** | Whether the supply is active or not | 

## Example

```python
from eZmaxApi.models.supply_autocomplete_element_response import SupplyAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyAutocompleteElementResponse from a JSON string
supply_autocomplete_element_response_instance = SupplyAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(SupplyAutocompleteElementResponse.to_json())

# convert the object into a dict
supply_autocomplete_element_response_dict = supply_autocomplete_element_response_instance.to_dict()
# create an instance of SupplyAutocompleteElementResponse from a dict
supply_autocomplete_element_response_from_dict = SupplyAutocompleteElementResponse.from_dict(supply_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


