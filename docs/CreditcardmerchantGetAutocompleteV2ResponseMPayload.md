# CreditcardmerchantGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/creditcardmerchant/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_creditcardmerchant** | [**List[CreditcardmerchantAutocompleteElementResponse]**](CreditcardmerchantAutocompleteElementResponse.md) | An array of Creditcardmerchant autocomplete element response. | 

## Example

```python
from eZmaxApi.models.creditcardmerchant_get_autocomplete_v2_response_m_payload import CreditcardmerchantGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardmerchantGetAutocompleteV2ResponseMPayload from a JSON string
creditcardmerchant_get_autocomplete_v2_response_m_payload_instance = CreditcardmerchantGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CreditcardmerchantGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
creditcardmerchant_get_autocomplete_v2_response_m_payload_dict = creditcardmerchant_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of CreditcardmerchantGetAutocompleteV2ResponseMPayload from a dict
creditcardmerchant_get_autocomplete_v2_response_m_payload_from_dict = CreditcardmerchantGetAutocompleteV2ResponseMPayload.from_dict(creditcardmerchant_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


