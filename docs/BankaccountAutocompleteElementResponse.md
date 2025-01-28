# BankaccountAutocompleteElementResponse

A Bankaccount AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_bankaccount_id** | **int** | The unique ID of the Bankaccount | 
**s_bankaccount_bankname** | **str** | The name of the bank | 
**b_bankaccount_isactive** | **bool** | Whether the Bankaccount is active or not | 

## Example

```python
from eZmaxApi.models.bankaccount_autocomplete_element_response import BankaccountAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountAutocompleteElementResponse from a JSON string
bankaccount_autocomplete_element_response_instance = BankaccountAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(BankaccountAutocompleteElementResponse.to_json())

# convert the object into a dict
bankaccount_autocomplete_element_response_dict = bankaccount_autocomplete_element_response_instance.to_dict()
# create an instance of BankaccountAutocompleteElementResponse from a dict
bankaccount_autocomplete_element_response_from_dict = BankaccountAutocompleteElementResponse.from_dict(bankaccount_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


