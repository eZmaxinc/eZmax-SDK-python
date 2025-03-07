# PaymentgatewayGetObjectV2ResponseMPayload

Payload for GET /2/object/paymentgateway/{pkiPaymentgatewayID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_paymentgateway** | [**PaymentgatewayResponseCompound**](PaymentgatewayResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.paymentgateway_get_object_v2_response_m_payload import PaymentgatewayGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayGetObjectV2ResponseMPayload from a JSON string
paymentgateway_get_object_v2_response_m_payload_instance = PaymentgatewayGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
paymentgateway_get_object_v2_response_m_payload_dict = paymentgateway_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of PaymentgatewayGetObjectV2ResponseMPayload from a dict
paymentgateway_get_object_v2_response_m_payload_from_dict = PaymentgatewayGetObjectV2ResponseMPayload.from_dict(paymentgateway_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


