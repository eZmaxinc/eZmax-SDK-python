# PeriodAutocompleteElementResponse

A Period AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_period_yyyymm** | **str** | The YYYYMM of the Period | 
**pki_period_id** | **int** | The unique ID of the Period | 
**b_period_isactive** | **bool** | Whether the Period is active or not | 

## Example

```python
from eZmaxApi.models.period_autocomplete_element_response import PeriodAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodAutocompleteElementResponse from a JSON string
period_autocomplete_element_response_instance = PeriodAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print PeriodAutocompleteElementResponse.to_json()

# convert the object into a dict
period_autocomplete_element_response_dict = period_autocomplete_element_response_instance.to_dict()
# create an instance of PeriodAutocompleteElementResponse from a dict
period_autocomplete_element_response_form_dict = period_autocomplete_element_response.from_dict(period_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


