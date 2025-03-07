# PaymentgatewayCreateObjectV1Response

Response for POST /1/object/paymentgateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymentgatewayCreateObjectV1ResponseMPayload**](PaymentgatewayCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentgateway_create_object_v1_response import PaymentgatewayCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayCreateObjectV1Response from a JSON string
paymentgateway_create_object_v1_response_instance = PaymentgatewayCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayCreateObjectV1Response.to_json())

# convert the object into a dict
paymentgateway_create_object_v1_response_dict = paymentgateway_create_object_v1_response_instance.to_dict()
# create an instance of PaymentgatewayCreateObjectV1Response from a dict
paymentgateway_create_object_v1_response_from_dict = PaymentgatewayCreateObjectV1Response.from_dict(paymentgateway_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


