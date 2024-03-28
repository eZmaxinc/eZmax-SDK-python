# BillingentityexternalAutocompleteElementResponse

A Billingentityexternal AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityexternal_id** | **int** | The unique ID of the Billingentityexternal | 
**s_billingentityexternal_description** | **str** | The description of the Billingentityexternal | 
**b_billingentityexternal_isactive** | **bool** | Whether the Billingentityexternal is active or not | 

## Example

```python
from eZmaxApi.models.billingentityexternal_autocomplete_element_response import BillingentityexternalAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityexternalAutocompleteElementResponse from a JSON string
billingentityexternal_autocomplete_element_response_instance = BillingentityexternalAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(BillingentityexternalAutocompleteElementResponse.to_json())

# convert the object into a dict
billingentityexternal_autocomplete_element_response_dict = billingentityexternal_autocomplete_element_response_instance.to_dict()
# create an instance of BillingentityexternalAutocompleteElementResponse from a dict
billingentityexternal_autocomplete_element_response_form_dict = billingentityexternal_autocomplete_element_response.from_dict(billingentityexternal_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


