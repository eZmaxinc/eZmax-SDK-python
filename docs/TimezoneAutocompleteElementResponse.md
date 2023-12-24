# TimezoneAutocompleteElementResponse

A Timezone AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_timezone_name** | **str** | The description of the Timezone | 
**pki_timezone_id** | **int** | The unique ID of the Timezone | 
**b_timezone_isactive** | **bool** | Whether the Timezone is active or not | 

## Example

```python
from eZmaxApi.models.timezone_autocomplete_element_response import TimezoneAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneAutocompleteElementResponse from a JSON string
timezone_autocomplete_element_response_instance = TimezoneAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print TimezoneAutocompleteElementResponse.to_json()

# convert the object into a dict
timezone_autocomplete_element_response_dict = timezone_autocomplete_element_response_instance.to_dict()
# create an instance of TimezoneAutocompleteElementResponse from a dict
timezone_autocomplete_element_response_form_dict = timezone_autocomplete_element_response.from_dict(timezone_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


