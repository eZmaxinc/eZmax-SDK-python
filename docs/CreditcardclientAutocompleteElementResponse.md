# CreditcardclientAutocompleteElementResponse

A Creditcardclient AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardclient_id** | **int** | The unique ID of the Creditcardclient | 
**s_creditcardclient_description** | **str** | The description of the Creditcardclient | 

## Example

```python
from eZmaxApi.models.creditcardclient_autocomplete_element_response import CreditcardclientAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientAutocompleteElementResponse from a JSON string
creditcardclient_autocomplete_element_response_instance = CreditcardclientAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientAutocompleteElementResponse.to_json())

# convert the object into a dict
creditcardclient_autocomplete_element_response_dict = creditcardclient_autocomplete_element_response_instance.to_dict()
# create an instance of CreditcardclientAutocompleteElementResponse from a dict
creditcardclient_autocomplete_element_response_from_dict = CreditcardclientAutocompleteElementResponse.from_dict(creditcardclient_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


