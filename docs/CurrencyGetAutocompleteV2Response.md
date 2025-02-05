# CurrencyGetAutocompleteV2Response

Response for GET /2/object/currency/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CurrencyGetAutocompleteV2ResponseMPayload**](CurrencyGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.currency_get_autocomplete_v2_response import CurrencyGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyGetAutocompleteV2Response from a JSON string
currency_get_autocomplete_v2_response_instance = CurrencyGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(CurrencyGetAutocompleteV2Response.to_json())

# convert the object into a dict
currency_get_autocomplete_v2_response_dict = currency_get_autocomplete_v2_response_instance.to_dict()
# create an instance of CurrencyGetAutocompleteV2Response from a dict
currency_get_autocomplete_v2_response_from_dict = CurrencyGetAutocompleteV2Response.from_dict(currency_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


