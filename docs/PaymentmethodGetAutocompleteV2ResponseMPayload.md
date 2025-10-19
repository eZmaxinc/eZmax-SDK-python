# PaymentmethodGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/paymentmethod/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_paymentmethod** | [**List[PaymentmethodAutocompleteElementResponse]**](PaymentmethodAutocompleteElementResponse.md) | An array of Paymentmethod autocomplete element response. | 

## Example

```python
from eZmaxApi.models.paymentmethod_get_autocomplete_v2_response_m_payload import PaymentmethodGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentmethodGetAutocompleteV2ResponseMPayload from a JSON string
paymentmethod_get_autocomplete_v2_response_m_payload_instance = PaymentmethodGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PaymentmethodGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
paymentmethod_get_autocomplete_v2_response_m_payload_dict = paymentmethod_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of PaymentmethodGetAutocompleteV2ResponseMPayload from a dict
paymentmethod_get_autocomplete_v2_response_m_payload_from_dict = PaymentmethodGetAutocompleteV2ResponseMPayload.from_dict(paymentmethod_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


