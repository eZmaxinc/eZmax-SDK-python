# PaymentgatewayGetListV1Response

Response for GET /1/object/paymentgateway/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymentgatewayGetListV1ResponseMPayload**](PaymentgatewayGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentgateway_get_list_v1_response import PaymentgatewayGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentgatewayGetListV1Response from a JSON string
paymentgateway_get_list_v1_response_instance = PaymentgatewayGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymentgatewayGetListV1Response.to_json())

# convert the object into a dict
paymentgateway_get_list_v1_response_dict = paymentgateway_get_list_v1_response_instance.to_dict()
# create an instance of PaymentgatewayGetListV1Response from a dict
paymentgateway_get_list_v1_response_from_dict = PaymentgatewayGetListV1Response.from_dict(paymentgateway_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


