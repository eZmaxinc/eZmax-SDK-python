# BankaccountGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/bankaccount/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_bankaccount** | [**List[BankaccountAutocompleteElementResponse]**](BankaccountAutocompleteElementResponse.md) | An array of Bankaccount autocomplete element response. | 

## Example

```python
from eZmaxApi.models.bankaccount_get_autocomplete_v2_response_m_payload import BankaccountGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetAutocompleteV2ResponseMPayload from a JSON string
bankaccount_get_autocomplete_v2_response_m_payload_instance = BankaccountGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
bankaccount_get_autocomplete_v2_response_m_payload_dict = bankaccount_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of BankaccountGetAutocompleteV2ResponseMPayload from a dict
bankaccount_get_autocomplete_v2_response_m_payload_from_dict = BankaccountGetAutocompleteV2ResponseMPayload.from_dict(bankaccount_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


