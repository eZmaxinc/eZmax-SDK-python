# CountryAutocompleteElementResponse

A Country AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_country_id** | **int** | The unique ID of the Country.  Here are some common values (Complete list must be retrieved from API):  |Value|Description| |-|-| |1|Canada| |2|United-States| | 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | 
**s_country_shortname** | **str** | The shortname of the Country | 
**b_country_isactive** | **bool** | Whether the Country is active or not | 

## Example

```python
from eZmaxApi.models.country_autocomplete_element_response import CountryAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CountryAutocompleteElementResponse from a JSON string
country_autocomplete_element_response_instance = CountryAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(CountryAutocompleteElementResponse.to_json())

# convert the object into a dict
country_autocomplete_element_response_dict = country_autocomplete_element_response_instance.to_dict()
# create an instance of CountryAutocompleteElementResponse from a dict
country_autocomplete_element_response_form_dict = country_autocomplete_element_response.from_dict(country_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


