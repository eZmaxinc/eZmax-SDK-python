# CreditcardtypeAutocompleteElementResponse

Creditcardtype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_creditcardtype_name** | **str** | The name of the Creditcardtype | 
**pki_creditcardtype_id** | **int** | The unique ID of the Creditcardtype | 
**e_creditcardtype_codename** | [**FieldECreditcardtypeCodename**](FieldECreditcardtypeCodename.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardtype_autocomplete_element_response import CreditcardtypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardtypeAutocompleteElementResponse from a JSON string
creditcardtype_autocomplete_element_response_instance = CreditcardtypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(CreditcardtypeAutocompleteElementResponse.to_json())

# convert the object into a dict
creditcardtype_autocomplete_element_response_dict = creditcardtype_autocomplete_element_response_instance.to_dict()
# create an instance of CreditcardtypeAutocompleteElementResponse from a dict
creditcardtype_autocomplete_element_response_from_dict = CreditcardtypeAutocompleteElementResponse.from_dict(creditcardtype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


