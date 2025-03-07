# PaymentgatewayCreateObjectV1Request

Request for POST /1/object/paymentgateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_paymentgateway** | [**List[PaymentgatewayRequestCompound]**](PaymentgatewayRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.paymentgateway_create_object_v1_request import PaymentgatewayCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayCreateObjectV1Request from a JSON string
paymentgateway_create_object_v1_request_instance = PaymentgatewayCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayCreateObjectV1Request.to_json())

# convert the object into a dict
paymentgateway_create_object_v1_request_dict = paymentgateway_create_object_v1_request_instance.to_dict()
# create an instance of PaymentgatewayCreateObjectV1Request from a dict
paymentgateway_create_object_v1_request_from_dict = PaymentgatewayCreateObjectV1Request.from_dict(paymentgateway_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


