# CurrencyGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/currency/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_currency** | [**List[CurrencyAutocompleteElementResponse]**](CurrencyAutocompleteElementResponse.md) | An array of Currency autocomplete element response. | 

## Example

```python
from eZmaxApi.models.currency_get_autocomplete_v2_response_m_payload import CurrencyGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyGetAutocompleteV2ResponseMPayload from a JSON string
currency_get_autocomplete_v2_response_m_payload_instance = CurrencyGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CurrencyGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
currency_get_autocomplete_v2_response_m_payload_dict = currency_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of CurrencyGetAutocompleteV2ResponseMPayload from a dict
currency_get_autocomplete_v2_response_m_payload_from_dict = CurrencyGetAutocompleteV2ResponseMPayload.from_dict(currency_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


