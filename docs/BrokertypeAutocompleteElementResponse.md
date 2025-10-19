# BrokertypeAutocompleteElementResponse

A Brokertype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_brokertype_id** | **int** | The unique ID of the Brokertype | 
**s_brokertype_name_x** | **str** | The name of the Brokertype in the language of the requester | 
**b_brokertype_isactive** | **bool** | Whether the Brokertype is active or not | 

## Example

```python
from eZmaxApi.models.brokertype_autocomplete_element_response import BrokertypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrokertypeAutocompleteElementResponse from a JSON string
brokertype_autocomplete_element_response_instance = BrokertypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(BrokertypeAutocompleteElementResponse.to_json())

# convert the object into a dict
brokertype_autocomplete_element_response_dict = brokertype_autocomplete_element_response_instance.to_dict()
# create an instance of BrokertypeAutocompleteElementResponse from a dict
brokertype_autocomplete_element_response_from_dict = BrokertypeAutocompleteElementResponse.from_dict(brokertype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


