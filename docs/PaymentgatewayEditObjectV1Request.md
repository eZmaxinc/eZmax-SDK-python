# PaymentgatewayEditObjectV1Request

Request for PUT /1/object/paymentgateway/{pkiPaymentgatewayID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_paymentgateway** | [**PaymentgatewayRequestCompound**](PaymentgatewayRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.paymentgateway_edit_object_v1_request import PaymentgatewayEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayEditObjectV1Request from a JSON string
paymentgateway_edit_object_v1_request_instance = PaymentgatewayEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayEditObjectV1Request.to_json())

# convert the object into a dict
paymentgateway_edit_object_v1_request_dict = paymentgateway_edit_object_v1_request_instance.to_dict()
# create an instance of PaymentgatewayEditObjectV1Request from a dict
paymentgateway_edit_object_v1_request_from_dict = PaymentgatewayEditObjectV1Request.from_dict(paymentgateway_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


