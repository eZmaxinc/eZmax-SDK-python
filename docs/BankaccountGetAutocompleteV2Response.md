# BankaccountGetAutocompleteV2Response

Response for GET /2/object/bankaccount/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BankaccountGetAutocompleteV2ResponseMPayload**](BankaccountGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_get_autocomplete_v2_response import BankaccountGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetAutocompleteV2Response from a JSON string
bankaccount_get_autocomplete_v2_response_instance = BankaccountGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetAutocompleteV2Response.to_json())

# convert the object into a dict
bankaccount_get_autocomplete_v2_response_dict = bankaccount_get_autocomplete_v2_response_instance.to_dict()
# create an instance of BankaccountGetAutocompleteV2Response from a dict
bankaccount_get_autocomplete_v2_response_from_dict = BankaccountGetAutocompleteV2Response.from_dict(bankaccount_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


