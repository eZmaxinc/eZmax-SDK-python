# RealestateboardAutocompleteElementResponse

A Realestateboard AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_realestateboard_id** | **int** | The unique ID of the Realestateboard | 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | 
**s_realestateboard_name_x** | **str** | The name of the Realestateboard | 
**b_realestateboard_isactive** | **bool** | Whether the Agenttype is active or not | 

## Example

```python
from eZmaxApi.models.realestateboard_autocomplete_element_response import RealestateboardAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RealestateboardAutocompleteElementResponse from a JSON string
realestateboard_autocomplete_element_response_instance = RealestateboardAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(RealestateboardAutocompleteElementResponse.to_json())

# convert the object into a dict
realestateboard_autocomplete_element_response_dict = realestateboard_autocomplete_element_response_instance.to_dict()
# create an instance of RealestateboardAutocompleteElementResponse from a dict
realestateboard_autocomplete_element_response_from_dict = RealestateboardAutocompleteElementResponse.from_dict(realestateboard_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


