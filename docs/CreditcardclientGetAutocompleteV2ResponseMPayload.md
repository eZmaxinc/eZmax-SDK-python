# CreditcardclientGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/creditcardclient/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_creditcardclient** | [**List[CreditcardclientAutocompleteElementResponse]**](CreditcardclientAutocompleteElementResponse.md) | An array of Creditcardclient autocomplete element response. | 

## Example

```python
from eZmaxApi.models.creditcardclient_get_autocomplete_v2_response_m_payload import CreditcardclientGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientGetAutocompleteV2ResponseMPayload from a JSON string
creditcardclient_get_autocomplete_v2_response_m_payload_instance = CreditcardclientGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
creditcardclient_get_autocomplete_v2_response_m_payload_dict = creditcardclient_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of CreditcardclientGetAutocompleteV2ResponseMPayload from a dict
creditcardclient_get_autocomplete_v2_response_m_payload_form_dict = creditcardclient_get_autocomplete_v2_response_m_payload.from_dict(creditcardclient_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


