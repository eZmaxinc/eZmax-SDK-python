# CreditcardtypeGetAutocompleteV2Response

Response for GET /2/object/creditcardtype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**CreditcardtypeGetAutocompleteV2ResponseMPayload**](CreditcardtypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardtype_get_autocomplete_v2_response import CreditcardtypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardtypeGetAutocompleteV2Response from a JSON string
creditcardtype_get_autocomplete_v2_response_instance = CreditcardtypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardtypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
creditcardtype_get_autocomplete_v2_response_dict = creditcardtype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of CreditcardtypeGetAutocompleteV2Response from a dict
creditcardtype_get_autocomplete_v2_response_from_dict = CreditcardtypeGetAutocompleteV2Response.from_dict(creditcardtype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


