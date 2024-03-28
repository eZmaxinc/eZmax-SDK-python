# BillingentityinternalAutocompleteElementResponse

A Billingentityinternal AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | 
**b_billingentityinternal_isactive** | **bool** | Whether the Billingentityinternal is active or not | 

## Example

```python
from eZmaxApi.models.billingentityinternal_autocomplete_element_response import BillingentityinternalAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityinternalAutocompleteElementResponse from a JSON string
billingentityinternal_autocomplete_element_response_instance = BillingentityinternalAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(BillingentityinternalAutocompleteElementResponse.to_json())

# convert the object into a dict
billingentityinternal_autocomplete_element_response_dict = billingentityinternal_autocomplete_element_response_instance.to_dict()
# create an instance of BillingentityinternalAutocompleteElementResponse from a dict
billingentityinternal_autocomplete_element_response_form_dict = billingentityinternal_autocomplete_element_response.from_dict(billingentityinternal_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


