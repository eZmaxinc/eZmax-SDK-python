# PaymentgatewayEditObjectV1Response

Response for PUT /1/object/paymentgateway/{pkiPaymentgatewayID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.paymentgateway_edit_object_v1_response import PaymentgatewayEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayEditObjectV1Response from a JSON string
paymentgateway_edit_object_v1_response_instance = PaymentgatewayEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayEditObjectV1Response.to_json())

# convert the object into a dict
paymentgateway_edit_object_v1_response_dict = paymentgateway_edit_object_v1_response_instance.to_dict()
# create an instance of PaymentgatewayEditObjectV1Response from a dict
paymentgateway_edit_object_v1_response_from_dict = PaymentgatewayEditObjectV1Response.from_dict(paymentgateway_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


