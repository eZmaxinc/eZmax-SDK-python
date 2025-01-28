# CreditcardmerchantAutocompleteElementResponse

A Creditcardmerchant AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardmerchant_id** | **int** | The unique ID of the Creditcardmerchant | 
**s_creditcardmerchant_description** | **str** | The description of the Creditcardmerchant | 
**b_creditcardmerchant_isactive** | **bool** | Whether the creditcardmerchant is active or not | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_autocomplete_element_response import CreditcardmerchantAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantAutocompleteElementResponse from a JSON string
creditcardmerchant_autocomplete_element_response_instance = CreditcardmerchantAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantAutocompleteElementResponse.to_json())

# convert the object into a dict
creditcardmerchant_autocomplete_element_response_dict = creditcardmerchant_autocomplete_element_response_instance.to_dict()
# create an instance of CreditcardmerchantAutocompleteElementResponse from a dict
creditcardmerchant_autocomplete_element_response_from_dict = CreditcardmerchantAutocompleteElementResponse.from_dict(creditcardmerchant_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


