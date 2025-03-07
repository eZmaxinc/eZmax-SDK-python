# PaymentgatewayGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/paymentgateway/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_paymentgateway** | [**List[PaymentgatewayAutocompleteElementResponse]**](PaymentgatewayAutocompleteElementResponse.md) | An array of Paymentgateway autocomplete element response. | 

## Example

```python
from eZmaxApi.models.paymentgateway_get_autocomplete_v2_response_m_payload import PaymentgatewayGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayGetAutocompleteV2ResponseMPayload from a JSON string
paymentgateway_get_autocomplete_v2_response_m_payload_instance = PaymentgatewayGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
paymentgateway_get_autocomplete_v2_response_m_payload_dict = paymentgateway_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of PaymentgatewayGetAutocompleteV2ResponseMPayload from a dict
paymentgateway_get_autocomplete_v2_response_m_payload_from_dict = PaymentgatewayGetAutocompleteV2ResponseMPayload.from_dict(paymentgateway_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


